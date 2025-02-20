#!/bin/bash
echo "[*] Activation de JavaScript dans Adobe Reader..."

# Modifier les préférences d'Adobe Reader pour activer JavaScript
mkdir -p ~/.adobe/Acrobat/9.0/Preferences
echo "<?xml version='1.0'?>
<AcrobatPreferences>
  <JavaScriptPreferences>
    <bEnableJS>1</bEnableJS>
  </JavaScriptPreferences>
</AcrobatPreferences>" > ~/.adobe/Acrobat/9.0/Preferences/reader_prefs.xml

echo "[*] Lancement automatique du fichier PDF..."

# Lancer Adobe Reader avec un affichage virtuel
Xvfb :99 -screen 0 1024x768x16 &
export DISPLAY=:99
acroread /app/malicious.pdf
