#!/bin/sh
# Gera o executável em dist/ (rode dentro do .venv)
pip install -r requirements.txt 2>/dev/null
pip install pyinstaller
pyinstaller --onefile --noconsole --name ProjetoIi_Zonamorta camadas_geradas/app.py
