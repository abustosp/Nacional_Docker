docker compose up -d
sleep 30
docker exec -ti mysql bash -c "mysql -uroot -proot master < master/master.sql"