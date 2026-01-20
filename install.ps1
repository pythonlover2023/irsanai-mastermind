# IrsanAI CLI Installer for Windows
# The Gateway to the Real-Time Production Factory
Write-Host "[*] Initializing IrsanAI Environment..." -ForegroundColor Cyan

# 1. Check Python
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "[!] Python not found. Please install Python 3.10+ from python.org" -ForegroundColor Red
    Exit
}

# 2. Create Virtual Environment
Write-Host "[*] Creating Neural Network (VENV)..." -ForegroundColor Green
python -m venv .venv

# 3. Activate & Install
Write-Host "[*] Downloading Skills (Dependencies)..." -ForegroundColor Green
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# 4. Create Shortcut
 = New-Object -comObject WScript.Shell
 = .CreateShortcut("\Desktop\IrsanAI-CLI.lnk")
.TargetPath = "/data/data/com.termux/files/home/irsanai-cli\.venv\Scripts\python.exe"
.Arguments = "/data/data/com.termux/files/home/irsanai-cli\src\main.py"
.Description = "Start IrsanAI CLI"
.Save()

Write-Host "[SUCCESS] IrsanAI is ready. Check your Desktop for the shortcut." -ForegroundColor Magenta
Start-Sleep -Seconds 3
