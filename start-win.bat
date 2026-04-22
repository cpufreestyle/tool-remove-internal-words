@echo off
REM Windows 启动脚本

cd /d "%~dp0"

echo === 文档内部字样清除工具 (Windows) ===
echo.

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 未找到 Python
    echo 💡 请从 https://python.org 下载安装
    pause
    exit /b 1
)

REM 检查依赖
echo ^>^>^> 检查依赖...
pip show Pillow >nul 2>&1 || pip install -q Pillow
pip show python-docx >nul 2>&1 || pip install -q python-docx
pip show PyPDF2 >nul 2>&1 || pip install -q PyPDF2

REM 检查 Tesseract (可选)
where tesseract >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Tesseract 未安装，OCR 功能不可用
    echo 💡 从 https://github.com/UB-Mannheim/tesseract/wiki 下载
)

echo ^>^>^> 启动应用...
python document_cleaner_gui.py

pause
