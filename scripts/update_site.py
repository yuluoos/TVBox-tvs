#!/usr/bin/env python3
"""把一个新版本写进 GitHub Pages 落地页 docs/index.html 的下载区。

只替换 <!-- BEGIN:downloads --> 与 <!-- END:downloads --> 之间的内容，
页面其余部分（SEO 元信息、功能、FAQ、结构化数据）保持手工维护。
由 scripts/release.sh 调用，也可单独跑。
"""

import argparse
import io
import json
import re
import sys

REPO = 'yuluoos/TVBox-tvs'
ABI_LABELS = ['arm64-v8a', 'armeabi-v7a', 'x86_64']
BEGIN = '<!-- BEGIN:downloads -->'
END = '<!-- END:downloads -->'


def download_url(version, filename):
    return f'https://github.com/{REPO}/releases/download/v{version}/{filename}'


def build_block(version, files):
    cards = []

    if 'arm64-v8a' in files:
        alts = ' '.join(
            f'<a href="{download_url(version, files[abi]["name"])}">{abi}</a>'
            for abi in ABI_LABELS[1:]
            if abi in files
        )
        alts_html = f'\n    <div class="alts">\n      其他架构：\n      {alts}\n    </div>' if alts else ''
        cards.append(
            '  <div class="card">\n'
            '    <h3>Android / Android TV / 电视盒子</h3>\n'
            '    <p>绝大多数手机与盒子选 arm64-v8a；最低 Android 7.0</p>\n'
            f'    <a class="btn" href="{download_url(version, files["arm64-v8a"]["name"])}">下载 APK (arm64-v8a)</a>'
            f'{alts_html}\n'
            '  </div>'
        )

    if 'ipa' in files:
        cards.append(
            '  <div class="card">\n'
            '    <h3>iOS / iPadOS</h3>\n'
            '    <p>自签名 IPA，需自行签名侧载（爱思、巨魔、AltStore、自签 API）</p>\n'
            f'    <a class="btn" href="{download_url(version, files["ipa"]["name"])}">下载 IPA</a>\n'
            '  </div>'
        )

    if 'dmg' in files:
        cards.append(
            '  <div class="card">\n'
            '    <h3>macOS（Apple Silicon）</h3>\n'
            '    <p>首次打开需在「隐私与安全性」中放行；仅 arm64</p>\n'
            f'    <a class="btn" href="{download_url(version, files["dmg"]["name"])}">下载 DMG</a>\n'
            '  </div>'
        )

    return (
        f'{BEGIN}\n'
        f'<h2 id="download">下载最新版 {version}</h2>\n'
        '<div class="grid">\n'
        + '\n'.join(cards) + '\n'
        '</div>\n'
        '<p style="font-size:14px;color:var(--muted)">全部版本、历史包与 SHA-256 校验值见\n'
        f'  <a href="https://github.com/{REPO}/releases">Releases 页面</a> 与\n'
        f'  <a href="https://github.com/{REPO}#版本记录">版本记录</a>。</p>\n'
        f'{END}'
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', required=True)
    parser.add_argument('--artifacts', required=True, help='产物 JSON：{kind: {name,size,sha256}}')
    parser.add_argument('--site', default='docs/index.html')
    args = parser.parse_args()

    files = json.loads(io.open(args.artifacts, encoding='utf-8').read())
    text = io.open(args.site, encoding='utf-8').read()

    pattern = re.compile(re.escape(BEGIN) + r'.*?' + re.escape(END), re.S)
    if not pattern.search(text):
        raise SystemExit(f'{args.site} 里找不到 {BEGIN} … {END} 标记')

    block = build_block(args.version, files)
    text = pattern.sub(lambda _: block, text, count=1)

    io.open(args.site, 'w', encoding='utf-8').write(text)
    print(f'docs/index.html 已更新到 {args.version}', file=sys.stderr)


if __name__ == '__main__':
    main()
