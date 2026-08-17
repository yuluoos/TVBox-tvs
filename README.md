# TVS — 聚合播放器

[![Release](https://img.shields.io/github/v/release/yuluoos/TVBox-tvs?label=release&color=blue)](https://github.com/yuluoos/TVBox-tvs/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/yuluoos/TVBox-tvs/total?label=downloads&color=success)](https://github.com/yuluoos/TVBox-tvs/releases)
[![Platform](https://img.shields.io/badge/platform-Android%20TV%20%7C%20Android%20%7C%20iOS%20%7C%20macOS-lightgrey)](https://github.com/yuluoos/TVBox-tvs/releases/latest)
[![Stars](https://img.shields.io/github/stars/yuluoos/TVBox-tvs?style=flat&color=yellow)](https://github.com/yuluoos/TVBox-tvs/stargazers)
[![License](https://img.shields.io/github/license/yuluoos/TVBox-tvs?color=informational)](LICENSE)

> TVBox 类空壳聚合播放器 · Flutter 跨平台 · Android TV / 电视盒子 / iOS / iPadOS / macOS · 提供 APK / IPA / DMG 直接下载
>
> A TVBox-style shell media player built with Flutter for Android TV, iOS and macOS — no built-in content, bring your own subscription and live sources.

## 下载（最新版 1.1.3）

| 平台 | 下载 | 说明 |
| --- | --- | --- |
| Android / Android TV / 电视盒子 | [arm64-v8a APK](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-1.1.3-arm64-v8a.apk) · [armeabi-v7a](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-1.1.3-armeabi-v7a.apk) · [x86_64](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-1.1.3-x86_64.apk) | 绝大多数设备选 arm64-v8a |
| iOS / iPadOS | [自签名 IPA](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-selfsign-1.1.3.ipa) | 需自行签名侧载（如爱思、巨魔、AltStore、自签 API） |
| macOS（Apple Silicon） | [DMG](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-1.1.3.dmg) | 首次打开需在「隐私与安全性」中放行 |

全部版本见 [Releases 页面](https://github.com/yuluoos/TVBox-tvs/releases)；历史版本与 SHA-256 校验值见文末[版本记录](#版本记录)。

---

TVS 是一款基于 Flutter 开发的跨平台（iOS / Android / macOS）聚合播放器，采用羊壳（PeekPili）一类的"空壳"设计：**应用本体不内置任何内容、频道或数据源**，安装后是一个空壳，所有内容均由用户自行导入订阅配置和直播源后才可用。**订阅仅适用于羊壳（PeekPili）格式**。应用只提供解析、聚合与播放能力，内容的可用性由用户导入的源决定。

本仓库用于管理 TVS 的打包产物（IPA / APK / DMG），版本记录见文末。

---

## 空壳设计说明

- 首次启动无任何内容，需在"订阅"页导入订阅配置；**仅支持羊壳（PeekPili）订阅**，其他格式的订阅不保证可用。
- 站点、分类、搜索结果、直播频道等全部来自用户导入的源，卸载配置即恢复空壳状态。
- 应用不提供、不推荐、不分发任何内容源，仅作为个人学习与技术研究用途。

## 功能介绍

### 订阅与源管理
- 支持导入羊壳（PeekPili）订阅配置，多订阅管理、切换当前生效配置。
- 内嵌本地服务运行爬虫源，完整支持 nodejs 类型 spider 站点。
- 应用前后台切换时自动检测并恢复本地服务，保证长时间使用稳定。

### 点播（VOD）
- **首页**：按当前配置的站点展示分类与推荐列表。
- **聚合搜索**：跨站点并发搜索，统一展示结果。
- **详情页**：剧集解析与展示，支持多线路 / 多集数结构。
- **解析播放**：支持播放地址解析（parse 接口），自动处理嗅探与防盗链请求头。

### 播放器
- 基于 media_kit（libmpv 内核）的高性能视频播放，支持主流格式与 m3u8 流。
- **片头片尾跳过**：按剧集记忆片头 / 片尾跳过秒数，本地持久化。
- **m3u8 广告过滤**：本地代理层对 m3u8 分片做过滤处理。
- **播放历史与断点续播**：自动记录观看进度，随时接续播放。
- 倍速、亮度 / 音量手势调节、播放时屏幕常亮。

### 直播（Live）
- 支持导入直播源，自动识别 **M3U / TXT（#genre# 分组）/ JSON** 三种格式。
- 频道分组浏览、台标显示、独立直播播放器。

### 听剧模式（音频播放）
- 独立音频播放页与全局迷你播放条，可后台播放（audio_service），息屏听剧。

### 本地代理服务
- 内置本地 HTTP 代理：图片防盗链代理、请求头转发、m3u8 过滤。

### TV / 遥控器适配
- 支持 D-pad 遥控器按键导航与焦点管理，适配 Android TV 使用场景。

### 其他
- 播放历史管理页、设置中心（含各功能项细分设置）。
- 数据本地存储（Isar 数据库 + 安全存储），无云端账号体系，隐私数据不出设备。

## 技术栈

基于 Flutter 开发，覆盖 iOS / Android / macOS；播放内核为 libmpv（media_kit），数据全部本地存储。

## 关键词 / Keywords

TVBox、tvbox 类客户端、空壳播放器、聚合播放器、电视盒子应用、Android TV 播放器、ATV apk、TV 版播放器、遥控器 D-pad 适配、羊壳、PeekPili 订阅、直播源播放器、M3U / IPTV 播放器、Flutter 播放器、media_kit、libmpv、nodejs spider 爬虫源、自签名 IPA、iOS 侧载、macOS DMG。

`tvbox` `android-tv` `iptv-player` `m3u` `flutter` `media-kit` `libmpv` `ipa` `apk` `dmg` `self-signed-ipa` `shell-player`

## 免责声明

本应用为空壳聚合播放器，不含任何内容与数据源。仅供个人学习、技术研究使用，请在遵守当地法律法规的前提下使用。

---

## 版本记录

### iOS（IPA）

| 版本 | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- |
| 1.1.3 (build 1) | [tvs-selfsign-1.1.3.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-selfsign-1.1.3.ipa) | 35 MB | `203ad19dc58599fd90c36213ea2f30c6d1a5be570cad440f8968d6de3f2a90b1` | 2026-08-17 |
| 1.1.2 (build 1) | [tvs-selfsign-1.1.2.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.2/tvs-selfsign-1.1.2.ipa) | 34 MB | `69013f6738b23cbf827ed2ea2e7852519e3bdbbafd80fbb7438f415c8c886bfc` | 2026-08-16 |
| 1.1.1 (build 1) | [tvs-selfsign-1.1.1.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-selfsign-1.1.1.ipa) | 34 MB | `d1eb718c7dba6b3342e024e24aea7db66470467e35533735337cb95eb4ae9313` | 2026-08-14 |

- IPA 为自签名（selfsign）Release 构建
- 每个版本对应一个 git tag（如 `v1.0.4`）
- 所有产物统一发布在 [GitHub Releases](https://github.com/yuluoos/TVBox-tvs/releases)，仓库内不再存放二进制文件
- 1.0.9 及更早版本的应用内更新检查读的是旧的 `releases/` 目录，该目录已移除，这些版本不会再弹出更新提示，请手动到 Releases 页面下载新版

### Android（APK）

按 ABI 分包，请按设备架构选择；绝大多数手机与电视盒子用 **arm64-v8a**。

| 版本 | ABI | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- | --- |
| 1.1.3 (build 1) | arm64-v8a | [tvs-1.1.3-arm64-v8a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-1.1.3-arm64-v8a.apk) | 33 MB | `124df400c24c7523c3f10a34f8595681c253e857b0bd84b0571f3bdaaff299aa` | 2026-08-17 |
| 1.1.3 (build 1) | armeabi-v7a | [tvs-1.1.3-armeabi-v7a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-1.1.3-armeabi-v7a.apk) | 32 MB | `72a7cb31e0a5416d655d2e4162df5afcee4b0b1c65d049e16b20ce18c386f816` | 2026-08-17 |
| 1.1.3 (build 1) | x86_64 | [tvs-1.1.3-x86_64.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-1.1.3-x86_64.apk) | 35 MB | `ea381d7a2bfffd830de32686e1e5238ea4b578a1b0d649ae4307047383173b1a` | 2026-08-17 |
| 1.1.2 (build 1) | arm64-v8a | [tvs-1.1.2-arm64-v8a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.2/tvs-1.1.2-arm64-v8a.apk) | 32 MB | `38a2a830f4f9f5e71cc95a4f1b7a4e3f0e42a53b713adb8f0dd871b126c58ba6` | 2026-08-16 |
| 1.1.2 (build 1) | armeabi-v7a | [tvs-1.1.2-armeabi-v7a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.2/tvs-1.1.2-armeabi-v7a.apk) | 31 MB | `95ca5e7584240dbf3d208ff8ff5d9c1596fda553c3dde3bb140b2c85eaa82682` | 2026-08-16 |
| 1.1.2 (build 1) | x86_64 | [tvs-1.1.2-x86_64.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.2/tvs-1.1.2-x86_64.apk) | 34 MB | `ea09cd74ca67f74d35e695e7c48db202ad33977a84d53719ecb42f072a7b742b` | 2026-08-16 |
| 1.1.1 (build 1) | arm64-v8a | [tvs-1.1.1-arm64-v8a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1-arm64-v8a.apk) | 32 MB | `5dd719102fd988bbe0c606c38b78837cabf905a16dc1a595f494df8cbfb00470` | 2026-08-14 |
| 1.1.1 (build 1) | armeabi-v7a | [tvs-1.1.1-armeabi-v7a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1-armeabi-v7a.apk) | 31 MB | `2d4e4f40a731186e10b017f6f0bba19da1aef9ac5ccc432acf46f132a1c623c4` | 2026-08-14 |
| 1.1.1 (build 1) | x86_64 | [tvs-1.1.1-x86_64.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1-x86_64.apk) | 34 MB | `98efbd857f6f03618097f7c2c96898c1f04b27afe34c42f6b20cbb35ccc4f3c6` | 2026-08-14 |

- 最低支持 Android 7.0（API 24），targetSdk 36
- APK 为 Release 构建，使用调试密钥签名，仅供侧载安装
- nodejs-mobile 上游无 32 位 x86 产物，故不提供 x86 包
- native 库采用压缩打包（`useLegacyPackaging`），安装时由系统解压，设备上会额外占用约 80 MB

### macOS（DMG）

| 版本 | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- |
| 1.1.3 (build 1) | [tvs-1.1.3.dmg](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.3/tvs-1.1.3.dmg) | 41 MB | `ceab134f780131b6c6289faf316eb15134f6a2854e2c980b49a9c4b1a3c967a5` | 2026-08-17 |
| 1.1.2 (build 1) | [tvs-1.1.2.dmg](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.2/tvs-1.1.2.dmg) | 41 MB | `d3af90b0f07f51a98aeaabfb35fff1356463915919d706e524956854b867e68e` | 2026-08-16 |
| 1.1.1 (build 1) | [tvs-1.1.1.dmg](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1.dmg) | 41 MB | `f21c427752730cd108989b201caf950a3b0f59e74e96ae94e6314e8d0445edc8` | 2026-08-14 |

- 仅提供 Apple Silicon（arm64）版本：内置的 Node 运行时上游只有 darwin-arm64 产物，Intel Mac 无法运行爬虫源
- DMG 使用 LZMA（ULMO）压缩，需 macOS 10.15+ 挂载
- 应用为 ad-hoc 自签名，首次打开会被 Gatekeeper 拦截；请在「访达」中右键点击 → 打开，或到「系统设置 → 隐私与安全性」中允许

### 1.1.3 更新内容

- **新增弹幕搜索与剧集匹配**：播放器弹幕面板支持按片名搜索弹幕库，并手动选择匹配的剧集加载弹幕
- 弹幕搜索接入弹弹play v2 搜索接口
- 优化 TV 端弹幕弹窗的遥控器交互与焦点体验

### 1.1.2 更新内容

- **Android 应用内直接更新**：发现新版本后可在弹窗点「立即更新」，应用自动下载对应 APK、校验 SHA-256 后调起系统安装器，无需再跳转 GitHub 手动下载（iOS / macOS 仍跳转 GitHub）
- **修复 spider 站点播放时片头广告未被过滤**：spider 本地代理产出的 HLS 流此前未经过 m3u8 广告过滤，现已正确接入
- 资源代理改为手动跟随重定向，每一跳都保留自定义请求头（User-Agent 等），修复部分防盗链站点播放失败
- 修复慢速设备上本地服务冷启动失败导致的站点加载异常

### 1.1.1 更新内容

本次为修复版本。

- **修复部分 AppV6 站点失效**：源站配置把旧站点键换成新键后，订阅里的旧站点解析不到而报错；现在会自动兼容回旧键，无需重新导入订阅
- 站点配置确实不兼容时，改为明确提示「站点配置不兼容，请刷新订阅后重试」，不再返回空结果或模糊报错
