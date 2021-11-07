# Distributed-System

This template used for front end: (https://colorlib.com)
This webapp is built using the python-flask framework with SQLite running in the back-end. 
The client interacts with the web UI to enter the information required to query about the climatic trends in different countries. 
This search query is also stored in the persistent database that does not get lost once the server restarts.

To run the application:

Change to the working directory

http://localhost:5001/publisher1
http://localhost:5002/subscriber1

**Docker Volume**
    docker volume create weather

**Copy the broker db file to volume , cd to Broker/**

    docker run -v weather:/data --name helper busybox true
    docker cp . helper:/data
    docker rm helper

docker-compose build
docker-compose up 

http://localhost:5001/publisher1 (Just one example for publisher1, it can be changed to publisher1-publisher12)
http://localhost:5002/subscriber1 (Just one example for subscriber1, it can be changed to subscriber1-subscriber12)

Type in the country name and choose the required options as per the drop down.

Hit submit

Scroll down to find the previously queried searches and it will have the searches stored in the database. 