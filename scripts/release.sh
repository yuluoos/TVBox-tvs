#!/bin/bash
# 一条命令走完发版：打包 → 建 GitHub Release → 更新 README → 提交推送。
#
# 用法：scripts/release.sh <version> <notes.md> [--skip-build] [--dry-run]
#   <version>     语义版本号，须与 tvs 源码仓库 pubspec.yaml 一致，如 1.1.0
#   <notes.md>    更新内容（Markdown 列表项），会同时写进 README 和 Release 正文
#   --skip-build  复用 tvs 仓库 build/ 下已有产物，不重新构建
#   --dry-run     只打包与生成改动，不建 Release、不提交、不推送
#
# 前置：gh 已登录；源码仓库在 $TVS_SRC（默认 ~/Desktop/GIt/tvs）。

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${TVS_SRC:-$HOME/Desktop/GIt/tvs}"
REPO="yuluoos/TVBox-tvs"
cd "$ROOT"

[[ $# -ge 2 ]] || { echo "用法：scripts/release.sh <version> <notes.md> [--skip-build] [--dry-run]" >&2; exit 1; }
VERSION="$1"
NOTES="$2"
shift 2

SKIP_BUILD=0
DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --skip-build) SKIP_BUILD=1 ;;
    --dry-run) DRY_RUN=1 ;;
    *) echo "错误：未知参数 $arg" >&2; exit 1 ;;
  esac
done

[[ "$VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo "错误：版本号格式应为 x.y.z" >&2; exit 1; }
[[ -f "$NOTES" ]] || { echo "错误：找不到更新内容文件 $NOTES" >&2; exit 1; }
[[ -d "$SRC" ]] || { echo "错误：找不到源码仓库 $SRC（可用 TVS_SRC 指定）" >&2; exit 1; }

PUBSPEC_VERSION=$(sed -n 's/^version: *\([^ +]*\).*/\1/p' "$SRC/pubspec.yaml")
BUILD_NUMBER=$(sed -n 's/^version: *[^+]*+\(.*\)/\1/p' "$SRC/pubspec.yaml")
[[ "$PUBSPEC_VERSION" == "$VERSION" ]] || {
  echo "错误：pubspec.yaml 是 $PUBSPEC_VERSION，与要发的 $VERSION 不一致" >&2; exit 1; }

if [[ -n $(git status --porcelain) ]]; then
  echo "错误：当前仓库有未提交改动，先处理干净再发版" >&2; exit 1
fi

# ---------- 打包 ----------
if [[ $SKIP_BUILD -eq 0 ]]; then
  echo "==> 打包 iOS 自签名 IPA"
  (cd "$SRC" && ./scripts/build_selfsign_ipa.sh)
  echo "==> 打包 Android APK（按 ABI 分包）"
  (cd "$SRC" && flutter build apk --release --split-per-abi)
  echo "==> 打包 macOS DMG"
  (cd "$SRC" && ./scripts/build_macos_dmg.sh)
fi

STAGE="$ROOT/.release-stage/$VERSION"
rm -rf "$STAGE"
mkdir -p "$STAGE"

collect() { # <源文件> <目标文件名>
  [[ -f "$1" ]] || { echo "错误：缺少产物 $1" >&2; exit 1; }
  cp "$1" "$STAGE/$2"
}

collect "$SRC/build/ios/tvs-selfsign-$VERSION.ipa" "tvs-selfsign-$VERSION.ipa"
collect "$SRC/build/macos/tvs-$VERSION.dmg" "tvs-$VERSION.dmg"
for abi in arm64-v8a armeabi-v7a x86_64; do
  collect "$SRC/build/app/outputs/flutter-apk/app-$abi-release.apk" "tvs-$VERSION-$abi.apk"
done

# ---------- 汇总校验值 ----------
ARTIFACTS="$STAGE/artifacts.json"
python3 - "$STAGE" "$VERSION" "$ARTIFACTS" <<'PY'
import hashlib, io, json, os, sys
stage, version, out = sys.argv[1], sys.argv[2], sys.argv[3]
kinds = {
    f'tvs-selfsign-{version}.ipa': 'ipa',
    f'tvs-{version}.dmg': 'dmg',
}
for abi in ('arm64-v8a', 'armeabi-v7a', 'x86_64'):
    kinds[f'tvs-{version}-{abi}.apk'] = abi

result = {}
for name, kind in kinds.items():
    path = os.path.join(stage, name)
    digest = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            digest.update(chunk)
    result[kind] = {
        'name': name,
        'size': round(os.path.getsize(path) / (1024 * 1024)),
        'sha256': digest.hexdigest(),
    }
io.open(out, 'w', encoding='utf-8').write(json.dumps(result, indent=2, ensure_ascii=False))
for kind, item in sorted(result.items()):
    print(f'{kind:12} {item["size"]:>3} MB  {item["sha256"]}')
PY

# ---------- 更新 README ----------
DATE=$(date +%Y-%m-%d)
python3 "$ROOT/scripts/update_readme.py" \
  --version "$VERSION" --date "$DATE" --build "${BUILD_NUMBER:-1}" \
  --notes-file "$NOTES" --artifacts "$ARTIFACTS"

# ---------- Release 正文 ----------
RELEASE_NOTES="$STAGE/release-notes.md"
python3 - "$NOTES" "$ARTIFACTS" "$RELEASE_NOTES" <<'PY'
import io, json, sys
notes = io.open(sys.argv[1], encoding='utf-8').read().strip()
files = json.loads(io.open(sys.argv[2], encoding='utf-8').read())
labels = {
    'arm64-v8a': 'Android / Android TV（多数设备）',
    'armeabi-v7a': 'Android（32 位）',
    'x86_64': 'Android（x86_64 模拟器 / 部分盒子）',
    'ipa': 'iOS / iPadOS（自签名）',
    'dmg': 'macOS（Apple Silicon）',
}
rows = ['', '## 下载', '', '| 平台 | 文件 | SHA-256 |', '| --- | --- | --- |']
for kind in ('arm64-v8a', 'armeabi-v7a', 'x86_64', 'ipa', 'dmg'):
    if kind not in files:
        continue
    item = files[kind]
    rows.append(f'| {labels[kind]} | {item["name"]} | `{item["sha256"]}` |')
io.open(sys.argv[3], 'w', encoding='utf-8').write(notes + '\n' + '\n'.join(rows) + '\n')
PY

if [[ $DRY_RUN -eq 1 ]]; then
  echo "==> dry-run：产物在 $STAGE，README 已改但未提交，Release 未创建"
  exit 0
fi

# ---------- 提交 README ----------
echo "==> 提交并推送 README"
git add README.md
git commit -m "Release tvs $VERSION"
git push origin main

# ---------- 建 Release ----------
echo "==> 创建 GitHub Release v$VERSION"
gh release create "v$VERSION" --repo "$REPO" --target main \
  --title "TVS $VERSION" --notes-file "$RELEASE_NOTES" --latest \
  "$STAGE"/tvs-*

rm -rf "$STAGE"
echo "==> 完成：https://github.com/$REPO/releases/tag/v$VERSION"
