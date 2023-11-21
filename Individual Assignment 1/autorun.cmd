@echo off
cd /d "%~dp0"   REM Change the directory to the location of this script

REM Try running the script using 'python'
python main.py

REM If 'python' command doesn't work, try 'py' as an alternative
if errorlevel 1 (
    py main.py
)

REM If 'py' command doesn't work, try 'python3' as an alternative
if errorlevel 1 (
    python3 main.py
)