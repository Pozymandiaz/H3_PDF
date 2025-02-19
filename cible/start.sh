#!/bin/bash

echo "[*] Lancement automatique du fichier PDF..."
acroread /app/malicious.pdf &
sleep 10  
tail -f /dev/null  
