# 文档内部字样清除工具

跨平台文档脱敏工具，支持 macOS、Windows、Linux。

## 功能特点

- ✅ 批量文件处理
- ✅ 文件状态标记（删除/保留）
- ✅ Word 文档支持 (.docx)
- ✅ PDF 文档支持
- ✅ 图片 OCR 文字识别
- ✅ 自定义替换规则
- ✅ 处理水印
- ✅ 跨平台支持

## 快速开始

### 方法 1: 直接运行 Python 脚本

```bash
# 安装依赖
pip install Pillow python-docx PyPDF2 pytesseract

# 运行
python document_cleaner_gui.py
```

### 方法 2: 打包成可执行文件

```bash
# 安装打包工具
pip install pyinstaller

# 打包
python build.py

# 输出在 dist/ 目录
```

## 平台说明

### macOS
- 输出: `dist/DocumentCleaner.app`
- 双击运行

### Windows
- 输出: `dist/DocumentCleaner.exe`
- 双击运行

### Linux
- 输出: `dist/DocumentCleaner`
- 运行: `./dist/DocumentCleaner`

## OCR 设置

图片文字识别需要安装 Tesseract OCR:

### macOS
```bash
brew install tesseract tesseract-lang
```

### Windows
下载安装: https://github.com/UB-Mannheim/tesseract/wiki

### Linux (Ubuntu/Debian)
```bash
sudo apt install tesseract-ocr tesseract-ocr-chi-sim
```

## 依赖库

- Pillow - 图片处理
- python-docx - Word 文档
- PyPDF2 - PDF 文档
- pytesseract - OCR 识别
- pyinstaller - 打包工具

## 使用方法

1. 点击「添加文件」或「添加文件夹」
2. 选择要处理的文件
3. 使用「标记删除」或「标记保留」
4. 点击「处理选中文件」
5. 查看结果并保存

## 替换规则

默认规则:
- 内部
- 机密
- 秘密
- 绝密

可在「设置」标签页自定义规则。

## 许可证

MIT License
