@echo off
cd /d "%~dp0"

pip show pyautogui >nul 2>&1
if %errorlevel% neq 0 (
    echo pyautogui bulunamadi, yukleniyor...
    pip install pyautogui
)

python main.py
pause