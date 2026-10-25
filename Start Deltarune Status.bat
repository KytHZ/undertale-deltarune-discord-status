@echo off
cd /d "%~dp0"
py -m pip install --user --quiet pypresence || python -m pip install --user --quiet pypresence
py deltarune_status.py || python deltarune_status.py
pause
