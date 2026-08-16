# TVS — 聚合播放器

[![Release](https://img.shields.io/github/v/release/yuluoos/TVBox-tvs?label=release&color=blue)](https://github.com/yuluoos/TVBox-tvs/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/yuluoos/TVBox-tvs/total?label=downloads&color=success)](https://github.com/yuluoos/TVBox-tvs/releases)
[![Platform](https://img.shields.io/badge/platform-Android%20TV%20%7C%20Android%20%7C%20iOS%20%7C%20macOS-lightgrey)](https://github.com/yuluoos/TVBox-tvs/releases/latest)
[![Stars](https://img.shields.io/github/stars/yuluoos/TVBox-tvs?style=flat&color=yellow)](https://github.com/yuluoos/TVBox-tvs/stargazers)
[![License](https://img.shields.io/github/license/yuluoos/TVBox-tvs?color=informational)](LICENSE)

> TVBox 类空壳聚合播放器 · Flutter 跨平台 · Android TV / 电视盒子 / iOS / iPadOS / macOS · 提供 APK / IPA / DMG 直接下载
>
> A TVBox-style shell media player built with Flutter for Android TV, iOS and macOS — no built-in content, bring your own subscription and live sources.

## 下载（最新版 1.1.1）

| 平台 | 下载 | 说明 |
| --- | --- | --- |
| Android / Android TV / 电视盒子 | [arm64-v8a APK](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1-arm64-v8a.apk) · [armeabi-v7a](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1-armeabi-v7a.apk) · [x86_64](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1-x86_64.apk) | 绝大多数设备选 arm64-v8a |
| iOS / iPadOS | [自签名 IPA](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-selfsign-1.1.1.ipa) | 需自行签名侧载（如爱思、巨魔、AltStore、自签 API） |
| macOS（Apple Silicon） | [DMG](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1.dmg) | 首次打开需在「隐私与安全性」中放行 |

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
| 1.1.1 (build 1) | [tvs-selfsign-1.1.1.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-selfsign-1.1.1.ipa) | 34 MB | `d1eb718c7dba6b3342e024e24aea7db66470467e35533735337cb95eb4ae9313` | 2026-08-14 |
| 1.1.0 (build 1) | [tvs-selfsign-1.1.0.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.0/tvs-selfsign-1.1.0.ipa) | 34 MB | `6e057af6646480a586f1336a0bf30531fb67c9bdc5b882defe4dbcc707103fa6` | 2026-08-14 |
| 1.0.9 (build 1) | [tvs-selfsign-1.0.9.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.9/tvs-selfsign-1.0.9.ipa) | 34 MB | `7b5427d4f06df3d121906f135cad60dcff4131013d4717d8c1073b5c6a477ce8` | 2026-08-13 |
| 1.0.8 (build 1) | [tvs-selfsign-1.0.8.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.8/tvs-selfsign-1.0.8.ipa) | 34 MB | `ab59b64f443c39dd82c4ffa6c5bcb75c7120a24d014ee5266b53c3016903cd5b` | 2026-08-13 |
| 1.0.7 (build 1) | [tvs-selfsign-1.0.7.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.7/tvs-selfsign-1.0.7.ipa) | 34 MB | `a2f7d00f3eb12029cdd3bad61e475b24342cba53449fba24962eebcbd65baf71` | 2026-08-12 |
| 1.0.6 (build 1) | [tvs-selfsign-1.0.6.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.6/tvs-selfsign-1.0.6.ipa) | 34 MB | `fabce9393dd54c9377292a5ef1f60b0489401d122b8d4caef49a42439c0f4df8` | 2026-08-11 |
| 1.0.5 (build 1) | [tvs-selfsign-1.0.5.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.5/tvs-selfsign-1.0.5.ipa) | 34 MB | `4ab15bdd956bbcf0183183403a8b2dcf98016e9a56432f1e9673a1dd5bc79262` | 2026-08-10 |
| 1.0.4 (build 1) | [tvs-selfsign-1.0.4.ipa](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.4/tvs-selfsign-1.0.4.ipa) | 34 MB | `fbf57c314393b09ee1e87beddb894a1907357a8107586fec479b3ea6e5a56e08` | 2026-08-09 |

- IPA 为自签名（selfsign）Release 构建
- 每个版本对应一个 git tag（如 `v1.0.4`）
- 所有产物统一发布在 [GitHub Releases](https://github.com/yuluoos/TVBox-tvs/releases)，仓库内不再存放二进制文件
- 1.0.9 及更早版本的应用内更新检查读的是旧的 `releases/` 目录，该目录已移除，这些版本不会再弹出更新提示，请手动到 Releases 页面下载新版

### Android（APK）

按 ABI 分包，请按设备架构选择；绝大多数手机与电视盒子用 **arm64-v8a**。

| 版本 | ABI | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- | --- |
| 1.1.1 (build 1) | arm64-v8a | [tvs-1.1.1-arm64-v8a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1-arm64-v8a.apk) | 32 MB | `5dd719102fd988bbe0c606c38b78837cabf905a16dc1a595f494df8cbfb00470` | 2026-08-14 |
| 1.1.1 (build 1) | armeabi-v7a | [tvs-1.1.1-armeabi-v7a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1-armeabi-v7a.apk) | 31 MB | `2d4e4f40a731186e10b017f6f0bba19da1aef9ac5ccc432acf46f132a1c623c4` | 2026-08-14 |
| 1.1.1 (build 1) | x86_64 | [tvs-1.1.1-x86_64.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1-x86_64.apk) | 34 MB | `98efbd857f6f03618097f7c2c96898c1f04b27afe34c42f6b20cbb35ccc4f3c6` | 2026-08-14 |
| 1.1.0 (build 1) | arm64-v8a | [tvs-1.1.0-arm64-v8a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.0/tvs-1.1.0-arm64-v8a.apk) | 32 MB | `b10ca1e80dd8e2c7d8c0c0122b5553994a958284d794ed876dbd2a283045cb79` | 2026-08-14 |
| 1.1.0 (build 1) | armeabi-v7a | [tvs-1.1.0-armeabi-v7a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.0/tvs-1.1.0-armeabi-v7a.apk) | 31 MB | `884df988673e767d67b3b89863f66280a5cb95ce1b931c65f9b273ceae14bc52` | 2026-08-14 |
| 1.1.0 (build 1) | x86_64 | [tvs-1.1.0-x86_64.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.0/tvs-1.1.0-x86_64.apk) | 34 MB | `d84ea6e8efff878d87ce60b582cadaec9a4264bf01cb94733b4ea13e773b27f4` | 2026-08-14 |
| 1.0.9 (build 1) | arm64-v8a | [tvs-1.0.9-arm64-v8a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.9/tvs-1.0.9-arm64-v8a.apk) | 32 MB | `b9759acdbfd328ef68cfcb92511b3c36741d215d654505337f974d554d0dded2` | 2026-08-13 |
| 1.0.9 (build 1) | armeabi-v7a | [tvs-1.0.9-armeabi-v7a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.9/tvs-1.0.9-armeabi-v7a.apk) | 31 MB | `23ba9892f7cb79ad93be6dad5b36b7cdfdbc3c74ce2ec9b885d8538295aa0ebd` | 2026-08-13 |
| 1.0.9 (build 1) | x86_64 | [tvs-1.0.9-x86_64.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.9/tvs-1.0.9-x86_64.apk) | 34 MB | `4d184042996dda6511e67e80fbc0f1ca6c9a6729ccaf56538add95065eed1400` | 2026-08-13 |
| 1.0.8 (build 1) | arm64-v8a | [tvs-1.0.8-arm64-v8a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.8/tvs-1.0.8-arm64-v8a.apk) | 32 MB | `acc2f3db4eb04f4980c8f9f31a6a78b2e23cc4a774774c35b3d36b2c7f5efc98` | 2026-08-13 |
| 1.0.8 (build 1) | armeabi-v7a | [tvs-1.0.8-armeabi-v7a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.8/tvs-1.0.8-armeabi-v7a.apk) | 31 MB | `ca05a484fe63662b2c7cdd6eadcfd356e19db07b62486fa953fea580672d6361` | 2026-08-13 |
| 1.0.8 (build 1) | x86_64 | [tvs-1.0.8-x86_64.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.8/tvs-1.0.8-x86_64.apk) | 34 MB | `adb0f0230bb4e087b1a766099ed41bb5dc2fd71c3943c9d7ace6faaf7deaae4d` | 2026-08-13 |
| 1.0.7 (build 1) | arm64-v8a | [tvs-1.0.7-arm64-v8a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.7/tvs-1.0.7-arm64-v8a.apk) | 32 MB | `42022bb707be6aa8d614fca70de4554fdf0940938b789dfc775fc2dc66f782e8` | 2026-08-12 |
| 1.0.7 (build 1) | armeabi-v7a | [tvs-1.0.7-armeabi-v7a.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.7/tvs-1.0.7-armeabi-v7a.apk) | 31 MB | `dbb8a484798c5673f76b736eab66b6a4d4753bfec2998278947b63fc56c8061a` | 2026-08-12 |
| 1.0.7 (build 1) | x86_64 | [tvs-1.0.7-x86_64.apk](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.7/tvs-1.0.7-x86_64.apk) | 34 MB | `20409fb22730743d0f172155daf3eb361f5af4288a9cb428d308d776e296a798` | 2026-08-12 |

- 最低支持 Android 7.0（API 24），targetSdk 36
- APK 为 Release 构建，使用调试密钥签名，仅供侧载安装
- nodejs-mobile 上游无 32 位 x86 产物，故不提供 x86 包
- native 库采用压缩打包（`useLegacyPackaging`），安装时由系统解压，设备上会额外占用约 80 MB

### macOS（DMG）

| 版本 | 文件 | 大小 | SHA-256 | 打包日期 |
| --- | --- | --- | --- | --- |
| 1.1.1 (build 1) | [tvs-1.1.1.dmg](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.1/tvs-1.1.1.dmg) | 41 MB | `f21c427752730cd108989b201caf950a3b0f59e74e96ae94e6314e8d0445edc8` | 2026-08-14 |
| 1.1.0 (build 1) | [tvs-1.1.0.dmg](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.1.0/tvs-1.1.0.dmg) | 41 MB | `b7f4e13a5bee60bd049086b4a556e078bdc2387d0b6d3af529afaa0048cb72fe` | 2026-08-14 |
| 1.0.9 (build 1) | [tvs-1.0.9.dmg](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.9/tvs-1.0.9.dmg) | 41 MB | `d599a4f8028a2c480cbcaa1085d0cd392f9f3eaff9e3c24c89bb9a2774758fe6` | 2026-08-13 |
| 1.0.8 (build 1) | [tvs-1.0.8.dmg](https://github.com/yuluoos/TVBox-tvs/releases/download/v1.0.8/tvs-1.0.8.dmg) | 41 MB | `fe5ebb213c7fd5c9bc5ab7802eb47c7a22e92b34222a70f28e8db2eaa243d5f5` | 2026-08-13 |

- 仅提供 Apple Silicon（arm64）版本：内置的 Node 运行时上游只有 darwin-arm64 产物，Intel Mac 无法运行爬虫源
- DMG 使用 LZMA（ULMO）压缩，需 macOS 10.15+ 挂载
- 应用为 ad-hoc 自签名，首次打开会被 Gatekeeper 拦截；请在「访达」中右键点击 → 打开，或到「系统设置 → 隐私与安全性」中允许

### 1.1.1 更新内容

本次为修复版本。

- **修复部分 AppV6 站点失效**：源站配置把旧站点键换成新键后，订阅里的旧站点解析不到而报错；现在会自动兼容回旧键，无需重新导入订阅
- 站点配置确实不兼容时，改为明确提示「站点配置不兼容，请刷新订阅后重试」，不再返回空结果或模糊报错

### 1.1.0 更新内容

本次以发布与更新方式的调整为主。

- **应用内更新检查改为读取 GitHub Releases**：不再扫描仓库目录，改为取最新 Release，弹窗直接展示该版本的更新说明
- 更新提示的「前往 GitHub」跳转到对应 Release 页面，可直接下载安装包
- 所有安装包（APK / IPA / DMG）统一发布在 GitHub Releases，仓库不再存放二进制文件
- 说明：1.0.9 及更早版本的应用内更新提示依赖已移除的旧目录，将不再弹出，请手动下载本版本

### 1.0.9 更新内容

本次以 TV 端播放稳定性与焦点体验为主，并新增版本更新提醒。

- **新增版本更新提醒**：应用会检查本仓库 `releases` 下的最新版本，有新版时弹窗提示并可一键前往 GitHub 下载；设置页也可手动检查
- Android TV 上关闭硬件解码，修复部分盒子花屏 / 黑屏与播放不稳定；设置页解码选项在 TV 上相应调整
- 修复 Android 视频与直播播放链路：播放器状态同步与直播控制器切换更稳定
- TV 播放器菜单无操作后自动隐藏，不再长期遮挡画面
- 修复 TV 上片头片尾跳过设置入口与对话框焦点
- 修复 TV 播放页返回时未回到详情页的问题（听剧页同样修正）
- TV 焦点视觉统一：首页、搜索、直播频道列表、设置、影片卡片与玻璃组件的焦点高亮更清晰一致

### 1.0.8 更新内容

本次以 TV / 遥控器体验为主。

- **新增手机扫码添加订阅**：电视端显示二维码与配对码，手机扫码后在网页填写订阅地址，经局域网直传到电视，链接 5 分钟有效，免去用遥控器输入长网址
- 配置中心改为内嵌 WebView 打开，电视上没有外部浏览器也能使用
- 全面梳理遥控器焦点：路由与主框架、玻璃弹窗、播放器对话框、播放器工具栏、直播页、听剧页控件均可用 D-pad 到达并操作
- 玻璃弹窗焦点隔离，方向键不再串到底层页面
- 视频画面与控件的焦点分离，工具栏获得焦点时高亮常驻可见
- 修复 Android TV 上需要按两次返回键才能退出的问题
- 退出播放页时正确停止音频播放
- 修复电视端对话框输入框的焦点导航
- 直播页焦点流转与控件操作改进
- 修复 iOS 上来电等中断结束后音频不自动恢复
- 优化 Android 启动图标，补齐自适应图标
- **新增 macOS 版本**：内嵌 Node 运行时，桌面端同样支持 nodejs 类型 spider 站点；产物瘦身为纯 arm64 并重新签名，安装包约 41 MB

### 1.0.7 更新内容

- 音频播放接入系统中断与音频焦点协调：来电、其他应用抢占后自动暂停，中断结束后恢复播放
- 切集时立即隔离并停止上一个播放源，避免解析较慢时上一集仍在后台发声
- 多次快速切集不再按数据库写入顺序倒序生效
- 仅在播放进度超过 90% 时判定为播放完成，修复加载失败被误判「完成」导致的连续空切下一集
- 音频播放遇到瞬时错误时留出缓冲期自动恢复，不再直接中断整段播放
- 播放器事件订阅按播放源代次隔离，旧播放源的回调不再影响新播放
- 听剧页补充加载中与错误状态展示，不再是空白页
- 视频续播与片头跳过改为等待有效时长后执行，避免打开媒体期间的事件被丢弃
- 播放器浮层进度控件重构，手势拖动进度显示更准确
- Android 增加 WAKE_LOCK 权限，后台听剧更稳定
- Android 首次提供 APK 发布包，native 库改为压缩打包，安装包由约 88 MB 降至约 33 MB

### 1.0.6 更新内容

- 界面统一为暗色液态玻璃风格：播放器浮层、选集面板、直播频道列表与全应用弹窗
- 首页默认选中第一个分类并展示筛选栏，筛选项不再重复；首个分类改为后台加载，进入更快
- 站点切换失败时保留原有首页内容，不再清空
- 直播频道列表打开时自动定位到当前频道
- 竖屏短剧支持上下滑动切集
- 音频播放支持列表循环 / 单曲循环 / 随机播放
- 长文本改为单行展示，放不下时自动滚动
- 修复设置页解码与网络配置不生效的问题
- 修复歌单封面在首页与播放相关界面不显示
- 焦点高亮效果仅在 TV 端展示
- 站点错误提示更可读（Node 403 转换、ECONNRESET 按错误码降级）
- 兼容 AppV6 符号键 ext 解码失败的订阅
- 无订阅时不再误报本地服务恢复失败
- Android 构建增加 x86_64 ABI 支持
- 修复外部 HLS 相对地址播放失败
- 修复本地播放请求头处理与搜索页卸载异常
- 修复悦听播放兼容与音频分流问题
- 优化密集弹幕的轨道分配

### 1.0.5 更新内容

- 修复闪退后本地服务恢复失败的问题
- 加固 m3u8 广告过滤与资源代理
- 首页重试时显示加载指示
- 优化核心数据加载链路
