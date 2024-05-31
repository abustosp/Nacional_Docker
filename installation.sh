apt update && apt install docker.io docker-compose-v2 -y
docker compose up -d
sleep 15
python3 listador-sql.py
bash creardb.sh
bash importar.sh
