#!/bin/bash

BASE_DIR=$(pwd)
METRICS_FILE="$BASE_DIR/logs/metrics.txt"

echo "===================================================="
echo " Starting NetPulse Network Scanner..."
echo "===================================================="

# Lista de alvos para monitorar: Nome|IP_ou_URL
TARGETS=(
    "Google_DNS|8.8.8.8"
    "Cloudflare_DNS|1.1.1.1"
    "Unifor_Portal|www.unifor.br"
    "Broken_Server|192.0.2.1"
)

# Limpa o arquivo de métricas da rodada anterior
> "$METRICS_FILE"

for ITEM in "${TARGETS[@]}"; do
    NAME=$(echo "$ITEM" | cut -d'|' -f1)
    HOST=$(echo "$ITEM" | cut -d'|' -f2)
    
    echo "[SCANNING] Testing connectivity for $NAME ($HOST)..."
    
    # Executa 2 pings rápidos esperando no máximo 2 segundos por resposta
    # Extrai a latência média usando o comando 'awk' do Linux
    PING_RESULT=$(ping -c 2 -W 2 "$HOST" 2>&1)
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        STATUS="ONLINE"
        # Captura a latência média (rtt min/avg/max/mdev)
        LATENCY=$(echo "$PING_RESULT" | tail -n 1 | cut -d'/' -f5)
    else
        STATUS="OFFLINE"
        LATENCY="0.0"
    fi
    
    # Salva no arquivo de texto estruturado para o Python ler
    echo "$NAME|$HOST|$STATUS|$LATENCY" >> "$METRICS_FILE"
done

echo "[SHELL SUCCESS] Metrics collected. Invoking Python UI generator..."
python3 "$BASE_DIR/generate_report.py"