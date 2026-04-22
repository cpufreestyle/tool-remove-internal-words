#!/bin/bash
# 启动文档内部字样清除工具 GUI 版本

cd "$(dirname "$0")"

# 检查 Python 3
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到 Python 3"
    exit 1
fi

# 检查并安装依赖
echo "检查依赖..."
pip3 install -q Pillow pytesseract python-docx PyPDF2 2>/dev/null || true

# 启动 GUI
python3 document_cleaner_gui.py
