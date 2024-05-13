apt update && apt install docker.io docker-compose-v2 -y
docker compose up -d
sleep 60
docker exec -ti mysql bash -c "mysql -uroot -proot master < master/master.sql"