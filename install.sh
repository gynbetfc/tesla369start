#!/bin/bash
echo "⚡ TESLA 369 BOT"
echo "================"
pkill -f python 2>/dev/null
sleep 1
echo "📦 Atualizando..."
pkg update -y -qq && pkg upgrade -y -qq
echo "🐍 Python..."
pkg install python -y -qq
echo "📦 Dependencias..."
pip install -q flask api-iqoption-faria requests
echo "🚀 Iniciando..."
python <(curl -s https://raw.githubusercontent.com/gynbetfc/tesla369start/main/boot.py)
echo ""
echo "✅ Pronto!"
while true; do sleep 60; done
