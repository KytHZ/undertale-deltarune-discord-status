@echo off
cd /d "%~dp0"
py -m pip install --user --quiet pypresence || python -m pip install --user --quiet pypresence
py undertale_status.py || python undertale_status.py
pause
