$ErrorActionPreference = "Stop"

if ($null -eq (Get-ChildItem env:VIRTUAL_ENV -ErrorAction SilentlyContinue))
{
    Write-Output "This script requires that the Bytecash Python virtual environment is activated."
    Write-Output "Execute '.\venv\Scripts\Activate.ps1' before running."
    Exit 1
}

if ($null -eq (Get-Command node -ErrorAction SilentlyContinue))
{
    Write-Output "Unable to find Node.js"
    Exit 1
}

Write-Output "Running 'git submodule update --init --recursive'."
Write-Output ""
git submodule update --recursive

Push-Location
try {
    Set-Location bytecash-blockchain-gui

    $ErrorActionPreference = "SilentlyContinue"
    npm install --loglevel=error
    npm audit fix
    npm run build
    py ..\installhelper.py

    Write-Output ""
    Write-Output "Bytecash blockchain Install-gui.ps1 completed."
    Write-Output ""
    Write-Output "Type 'cd bytecash-blockchain-gui' and then 'npm run electron' to start the GUI."
} finally {
    Pop-Location
}
