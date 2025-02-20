#!/bin/bash

echo "[*] Lancement automatique du fichier PDF..."

# Lancer Adobe Reader avec un affichage virtuel
Xvfb :99 -screen 0 1024x768x16 &
export DISPLAY=:99
wine AcroRd8.exe /app/malicious.pdf

