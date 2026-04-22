#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
跨平台打包脚本
支持 macOS, Windows, Linux
"""

import os
import sys
import platform
import subprocess
import shutil

PLATFORM = platform.system()
IS_MAC = PLATFORM == 'Darwin'
IS_WINDOWS = PLATFORM == 'Windows'
IS_LINUX = PLATFORM == 'Linux'

print(f"=== 文档内部字样清除工具 - 打包脚本 ===")
print(f"平台: {PLATFORM} ({platform.machine()})")
print()

# 安装依赖
print(">>> 安装依赖...")
deps = ['pyinstaller', 'Pillow', 'python-docx', 'PyPDF2', 'pytesseract']
subprocess.run([sys.executable, '-m', 'pip', 'install'] + deps, check=False)

# 打包参数
APP_NAME = "DocumentCleaner"
MAIN_SCRIPT = "document_cleaner_gui.py"

# 基础参数
cmd = [
    sys.executable, '-m', 'PyInstaller',
    '--onefile',
    '--windowed',
    '--name', APP_NAME,
    '--clean',
]

# 平台特定参数
if IS_MAC:
    cmd.extend([
        '--icon', 'icon.icns',  # 如果有图标
        '--osx-bundle-identifier', 'com.qclaw.documentcleaner',
    ])
    output_ext = '.app'
elif IS_WINDOWS:
    cmd.extend([
        '--icon', 'icon.ico',  # 如果有图标
    ])
    output_ext = '.exe'
else:
    output_ext = ''

# 添加主脚本
cmd.append(MAIN_SCRIPT)

print(f">>> 打包命令: {' '.join(cmd)}")
print()

# 执行打包
result = subprocess.run(cmd)

if result.returncode == 0:
    print()
    print("✅ 打包成功！")
    
    # 输出文件位置
    dist_dir = 'dist'
    output_file = os.path.join(dist_dir, APP_NAME + output_ext)
    
    if os.path.exists(output_file):
        print(f"📦 输出文件: {os.path.abspath(output_file)}")
        
        # 文件大小
        if os.path.isfile(output_file):
            size = os.path.getsize(output_file)
            print(f"📊 文件大小: {size / 1024 / 1024:.1f} MB")
        elif os.path.isdir(output_file):
            # macOS .app 是目录
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(output_file):
                for f in filenames:
                    total_size += os.path.getsize(os.path.join(dirpath, f))
            print(f"📊 应用大小: {total_size / 1024 / 1024:.1f} MB")
    
    print()
    print(">>> 清理临时文件...")
    if os.path.exists('build'):
        shutil.rmtree('build')
    if os.path.exists(f'{APP_NAME}.spec'):
        os.remove(f'{APP_NAME}.spec')
    
    print("✅ 清理完成！")
else:
    print("❌ 打包失败！")
    sys.exit(1)
