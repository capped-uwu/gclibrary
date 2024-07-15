@echo off
setlocal

set PYTHON_VERSION=3.12.4

if "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe
) else (
    set PYTHON_INSTALLER=python-%PYTHON_VERSION%.exe
)
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%

python --version >nul 2>&1
if %errorlevel% neq 0 (

    powershell -Command "Invoke-WebRequest -Uri %PYTHON_URL% -OutFile %PYTHON_INSTALLER%"

    start /wait "" %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1

    del %PYTHON_INSTALLER%

    python --version
    if %errorlevel% neq 0 (
        exit /b 1
    )
) else (
    python --version
)

if exist req.txt (
    py -m pip install -r req.txt
    if %errorlevel% neq 0 (
        exit /b 1
    )
) else (
    exit /b 1
)

set PYTHON_SCRIPT=run.py
python %PYTHON_SCRIPT%

endlocal
exit /b 0
