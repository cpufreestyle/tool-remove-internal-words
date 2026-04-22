#!/bin/bash
# Linux 启动脚本

cd "$(dirname "$0")"

echo "=== 文档内部字样清除工具 (Linux) ==="
echo

# 检查 Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到 Python 3"
    echo "💡 请安装: sudo apt install python3 python3-pip"
    exit 1
fi

# 检查 tkinter
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ 未找到 tkinter"
    echo "💡 请安装: sudo apt install python3-tk"
    exit 1
fi

# 检查依赖
echo ">>> 检查依赖..."
pip3 show Pillow &> /dev/null || pip3 install -q Pillow
pip3 show python-docx &> /dev/null || pip3 install -q python-docx
pip3 show PyPDF2 &> /dev/null || pip3 install -q PyPDF2

# 检查 Tesseract (可选)
if ! command -v tesseract &> /dev/null; then
    echo "⚠️  Tesseract 未安装，OCR 功能不可用"
    echo "💡 安装: sudo apt install tesseract-ocr tesseract-ocr-chi-sim"
fi

echo ">>> 启动应用..."
python3 document_cleaner_gui.py
