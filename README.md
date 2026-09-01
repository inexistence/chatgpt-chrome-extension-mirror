# ChatGPT Chrome Extension Mirror

自动检查并归档 Chrome Web Store 中 ChatGPT 扩展的版本。项目是个人镜像，**不隶属于 OpenAI**。

## 安装方式

前往仓库的 [Releases](../../releases/latest) 页面，下载最新版本的 `chatgpt-extension.zip` 或 `chatgpt-extension.crx`。

### 方式一：加载 ZIP（推荐）

1. 下载并解压 `chatgpt-extension.zip` 到一个固定目录。不要只打开 ZIP 预览，也不要之后删除这个目录。
2. 在 Chrome 地址栏打开 `chrome://extensions`。
3. 打开右上角的“开发者模式”。
4. 点击“加载已解压的扩展程序”。
5. 选择刚才解压出的目录（该目录中应直接包含 `manifest.json`）。

### 方式二：安装 CRX

1. 在 `chrome://extensions` 打开“开发者模式”。
2. 将 `chatgpt-extension.crx` 拖入扩展管理页面。
3. 如果 Chrome 拒绝安装，请改用上面的“加载已解压的扩展程序”方式；部分 Chrome 版本会限制从本地安装 CRX。

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

## 注意

请确认你所在地区、组织和 OpenAI/Chrome Web Store 的条款允许再分发该扩展。不要将本仓库描述成官方仓库。
