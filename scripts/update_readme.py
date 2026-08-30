#!/usr/bin/env python3
"""把一个新版本写进 README：下载区、三张版本表、更新内容段落。

由 scripts/release.sh 调用，也可单独跑（改错了直接 git checkout README.md 重来）。
"""

import argparse
import io
import json
import re
import sys

REPO = 'yuluoos/TVBox-tvs'
ABI_LABELS = ['arm64-v8a', 'armeabi-v7a', 'x86_64']


def download_url(version, filename):
    return f'https://github.com/{REPO}/releases/download/v{version}/{filename}'


def build_download_section(version, files):
    apk_links = ' · '.join(
        f'[{"arm64-v8a APK" if abi == "arm64-v8a" else abi}]({download_url(version, files[abi]["name"])})'
        for abi in ABI_LABELS
        if abi in files
    )
    rows = [
        '| 平台 | 下载 | 说明 |',
        '| --- | --- | --- |',
    ]
    if apk_links:
        rows.append(
            f'| Android / Android TV / 电视盒子 | {apk_links} | 绝大多数设备选 arm64-v8a |'
        )
    if 'ipa' in files:
        rows.append(
            f'| iOS / iPadOS | [自签名 IPA]({download_url(version, files["ipa"]["name"])}) '
            '| 需自行签名侧载（如爱思、巨魔、AltStore、自签 API） |'
        )
    if 'dmg' in files:
        rows.append(
            f'| macOS（Apple Silicon） | [DMG]({download_url(version, files["dmg"]["name"])}) '
            '| 首次打开需在「隐私与安全性」中放行 |'
        )
    return f'## 下载（最新版 {version}）\n\n' + '\n'.join(rows) + '\n'


def replace_download_section(text, version, files):
    pattern = re.compile(r'## 下载（最新版 [^）]+）\n\n(?:\|[^\n]*\n)+')
    section = build_download_section(version, files)
    if not pattern.search(text):
        raise SystemExit('README 里找不到「下载（最新版 …）」区块')
    return pattern.sub(lambda _: section, text, count=1)


def replace_rows(text, heading, rows):
    """用新行替换指定小节表格里的所有已有数据行。"""
    idx = text.index(heading)
    sep = text.index('| --- |', idx)
    data_start = text.index('\n', sep) + 1
    data_end = data_start
    while data_end < len(text) and text.startswith('|', data_end):
        line_end = text.find('\n', data_end)
        data_end = len(text) if line_end == -1 else line_end + 1
    return text[:data_start] + ''.join(row + '\n' for row in rows) + text[data_end:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', required=True)
    parser.add_argument('--date', required=True, help='打包日期，YYYY-MM-DD')
    parser.add_argument('--build', default='1')
    parser.add_argument('--notes-file', required=True, help='更新内容 Markdown（列表项）')
    parser.add_argument('--artifacts', required=True, help='产物 JSON：{kind: {name,size,sha256}}')
    parser.add_argument('--readme', default='README.md')
    args = parser.parse_args()

    files = json.loads(io.open(args.artifacts, encoding='utf-8').read())
    notes = io.open(args.notes_file, encoding='utf-8').read().strip()
    text = io.open(args.readme, encoding='utf-8').read()
    version, date, build = args.version, args.date, args.build

    if f'| {version} (build ' in text:
        raise SystemExit(f'README 里已经有 {version} 的记录，先清理再跑')

    text = replace_download_section(text, version, files)

    if 'ipa' in files:
        item = files['ipa']
        text = replace_rows(text, '### iOS（IPA）', [
            f'| {version} (build {build}) | [{item["name"]}]({download_url(version, item["name"])}) '
            f'| {item["size"]} MB | `{item["sha256"]}` | {date} |'
        ])

    apk_rows = [
        f'| {version} (build {build}) | {abi} | [{files[abi]["name"]}]({download_url(version, files[abi]["name"])}) '
        f'| {files[abi]["size"]} MB | `{files[abi]["sha256"]}` | {date} |'
        for abi in ABI_LABELS
        if abi in files
    ]
    if apk_rows:
        text = replace_rows(text, '### Android（APK）', apk_rows)

    if 'dmg' in files:
        item = files['dmg']
        text = replace_rows(text, '### macOS（DMG）', [
            f'| {version} (build {build}) | [{item["name"]}]({download_url(version, item["name"])}) '
            f'| {item["size"]} MB | `{item["sha256"]}` | {date} |'
        ])

    marker = re.search(r'^### \d+\.\d+\.\d+ 更新内容$', text, re.M)
    if not marker:
        raise SystemExit('README 里找不到任何「### x.y.z 更新内容」段落')
    next_heading = re.search(r'^## ', text[marker.end():], re.M)
    notes_end = len(text) if not next_heading else marker.end() + next_heading.start()
    suffix = text[notes_end:]
    text = text[: marker.start()] + f'### {version} 更新内容\n\n{notes}\n'
    if suffix:
        text += '\n' + suffix.lstrip('\n')

    io.open(args.readme, 'w', encoding='utf-8').write(text)
    print(f'README 已更新到 {version}', file=sys.stderr)


if __name__ == '__main__':
    main()
