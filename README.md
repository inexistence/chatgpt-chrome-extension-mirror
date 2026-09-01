# ChatGPT Chrome Extension Mirror

自动检查并归档 Chrome Web Store 中 ChatGPT 扩展的版本。项目是个人镜像，**不隶属于 OpenAI**。

## 使用方式

- `chatgpt-extension.crx`：原始 CRX 包。Chrome 可能要求开启开发者模式。
- `chatgpt-extension.zip`：解压后，在 `chrome://extensions` 开启“开发者模式”，选择“加载已解压的扩展程序”。
- `SHA256SUMS`：原始 CRX 的 SHA-256 校验值。

GitHub Actions 每天运行一次，也可以在 Actions 页面手动触发。只有检测到新版本时才会创建 Release。

## 注意

请确认你所在地区、组织和 OpenAI/Chrome Web Store 的条款允许再分发该扩展。不要将本仓库描述成官方仓库。

