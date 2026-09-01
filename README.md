# ChatGPT Chrome Extension Mirror

这是 Chrome Web Store 中 ChatGPT 官方浏览器扩展的个人镜像和版本归档，扩展 ID 为：

```text
hehggadaopoacecdllhhajmbjkdcmajg
```

项目通过 GitHub Actions 自动检查更新，并提供可下载的 CRX 和 ZIP 文件。项目本身是个人镜像，**不隶属于 OpenAI，也不是 OpenAI 的源码仓库**。

## 这个扩展是做什么的？

它用于在 Chrome 中使用 ChatGPT 的浏览器辅助能力，主要包括：

- 从 Chrome 侧边栏打开 ChatGPT；
- 在 `chatgpt.com` 页面提供 ChatGPT 相关的浏览器交互；
- 让 ChatGPT 在获得相应权限后执行部分浏览器操作，例如读取或操作标签页、历史记录、书签、下载等；
- 支持 ChatGPT/Codex 的浏览器工作流和本地辅助功能。

它不是一个独立的聊天网站，也不是 ChatGPT 网页客户端的替代品；使用时通常需要登录 ChatGPT，并按 Chrome 的提示授予必要权限。

如果你搜索的是“ChatGPT Chrome 插件”“ChatGPT 浏览器扩展”“OpenAI ChatGPT side panel”或“无法访问 Chrome Web Store 时安装 ChatGPT 扩展”，这个仓库就是用于下载和安装该扩展的镜像。

> 说明：Google Chrome 集成是 ChatGPT/Codex 桌面应用内置的浏览器功能，不是插件市场中可以单独搜索和安装的普通插件。这个仓库只提供 Chrome 扩展文件；要使用浏览器控制功能，仍需要安装 ChatGPT 桌面应用，并在“设置” → “Computer Use”中启用或管理 Google Chrome。

## 安装方式

前往仓库的 [Releases](../../releases/latest) 页面，下载最新版本的 `chatgpt-extension.crx`。只有在 CRX 无法安装时，才使用 ZIP 方式。

### 方式一：安装 CRX（推荐）

1. 在 `chrome://extensions` 打开“开发者模式”。
2. 将 `chatgpt-extension.crx` 拖入扩展管理页面。
3. 确认 Chrome 显示的扩展 ID 是 `hehggadaopoacecdllhhajmbjkdcmajg`。
4. 如果 Chrome 拒绝安装，请先卸载同名的已解压版本，再重启 Chrome 后重试。

### 方式二：加载 ZIP（备用）

1. 下载并解压 `chatgpt-extension.zip` 到一个固定目录。
2. 在 `chrome://extensions` 打开“开发者模式”。
3. 点击“加载已解压的扩展程序”，选择直接包含 `manifest.json` 的目录。
4. 本项目生成的 ZIP 会自动补入官方公钥，正常情况下应生成官方扩展 ID `hehggadaopoacecdllhhajmbjkdcmajg`。如果 Chrome 显示的是其他 ID，说明当前包没有保留官方身份，可能无法连接 ChatGPT 桌面应用的 Native Messaging Host。

### 校验下载文件（可选）

Release 中的 `SHA256SUMS` 对应原始 CRX 文件。macOS/Linux 可以运行：

```bash
sha256sum -c SHA256SUMS
```

macOS 若没有 `sha256sum`，可以运行：

```bash
shasum -a 256 -c SHA256SUMS
```

## 文件说明

- `chatgpt-extension.crx`：原始 CRX 包。
- `chatgpt-extension.zip`：可加载的已解压扩展文件包。
- `SHA256SUMS`：原始 CRX 的 SHA-256 校验值。

GitHub Actions 每天运行一次，也可以在 Actions 页面手动触发。只有检测到新版本时才会创建 Release。

## 连接不上 ChatGPT 桌面应用

如果侧边栏显示：`The Chrome side panel could not connect to the ChatGPT desktop app`，通常不是下载包损坏，而是扩展没有连接到本机的 ChatGPT 桌面应用。

请注意：仅安装本仓库提供的 CRX/ZIP 不足以启用完整功能。桌面应用会提供本机连接服务（Native Messaging Host），扩展通过它与 ChatGPT/Codex 通信；这个连接服务不会从 CRX/ZIP 中自动安装。

请依次检查：

1. 安装并更新 [ChatGPT 桌面应用](https://chatgpt.com/download/)。
2. 在桌面应用中打开“设置” → “Computer Use”，选择 Chrome，并完成连接/安装流程。
3. 确认扩展已在你实际使用的 Chrome 配置文件中启用；如果有多个 Chrome Profile，请在正确的 Profile 中安装。
4. 完全退出并重新打开 ChatGPT 桌面应用和 Chrome。
5. 如果桌面应用中的状态仍显示“Install”，重新执行连接流程，或删除扩展后再安装一次。

这个镜像只提供 Chrome 扩展文件，不能替代 ChatGPT 桌面应用或其本机连接服务。没有桌面应用时，扩展的侧边栏连接功能无法正常工作。更多背景和排障步骤参见 [OpenAI Browser extension 文档](https://developers.openai.com/codex/chrome-extension)。

## 注意

请确认你所在地区、组织和 OpenAI/Chrome Web Store 的条款允许再分发该扩展。不要将本仓库描述成官方仓库。
