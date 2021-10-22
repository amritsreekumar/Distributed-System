docker build -t flaskapp:latest .


docker volume create weather

docker network create --driver bridge weather-app-net


docker run -v weather:/data --name helper busybox true
(cd to broker folder)
docker cp . helper:/data
docker rm helper


docker build -t flaskapp:latest .
docker run -it -d -p 5001:5001 --name publisher --mount type=volume,source=weather,target=/app/data  --network weather-app-net flaskapp


docker build -t flaskapp:latest .
docker run -it -d -p 5002:5002 --name subscriber --network weather-app-net --mount type=volume,source=weather,target=/app/data flaskapp
