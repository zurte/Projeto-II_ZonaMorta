@echo off
REM Gera o executavel em dist\ (rode dentro do .venv)
pip install pyinstaller
pyinstaller --onefile --noconsole --name ProjetoIi_Zonamorta camadas_geradas/app.py
