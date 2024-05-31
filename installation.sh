#!/bin/bash

# Habilitar modo estricto para capturar errores y gestionar variables no definidas
set -euo pipefail

# Actualizar lista de paquetes e instalar Docker
echo "Actualizando lista de paquetes..."
sudo apt update

echo "Instalando docker.io y docker-compose-v2..."
sudo apt install -y docker.io docker-compose-v2

# Levantar los contenedores Docker
echo "Levantando los contenedores Docker..."
docker compose up -d

# Esperar 15 segundos
echo "Esperando 15 segundos para asegurar que los contenedores se han levantado..."
sleep 15

# Ejecutar script de Python
echo "Ejecutando listador-sql.py..."
python3 listador-sql.py

# Ejecutar scripts Bash
echo "Ejecutando creardb.sh..."
bash creardb.sh

echo "Ejecutando importar.sh..."
bash importar.sh

echo "Proceso completado."

