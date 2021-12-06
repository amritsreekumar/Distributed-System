# Distributed-System

This template used for front end: (https://colorlib.com)
This webapp is built using the python-flask framework with SQLite running in the back-end. 
The client interacts with the web UI to enter the information required to query about the climatic trends in different countries. 
This search query is also stored in the persistent database that does not get lost once the server restarts.

To run the application:

In order for the brokers to share the same db, we have made use of docker volume and its, attached with just the brokers.
**Docker Volume**
    docker volume create weather

**Copy the broker db file to volume**
    cd Broker/
    docker run -v weather:/data --name helper busybox true
    docker cp . helper:/data
    docker rm helper

To start the dockers, we have written a docker compose file, so that the 3 brokers and publisher and subscriber dockers starts with just one line of code


To build the docker

    cd ..
    docker-compose build

To compose the docker

    docker-compose up 

Example links:
        
        http://localhost:5001/publisher1 (Just one example for publisher1, it can be changed to publisher1-publisher12)
        
        http://localhost:5002/subscriber1 (Just one example for subscriber1, it can be changed to subscriber1-subscriber12)


Type in the country name and choose the required options as per the drop down.

Hit submit

Scroll down to find the previously queried searches and it will have the searches stored in the database along with the published data as per the subscription. 

brew install kafka
brew install zookeeper

To start zookeeper now and restart at login:
  brew services start zookeeper
Or, if you don't want/need a background service you can just run:
  zkServer start

To restart kafka after an upgrade:
  brew services restart kafka
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/kafka/bin/kafka-server-start /opt/homebrew/etc/kafka/server.properties


kafka-topics --create --topic test-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 4 

kafka-console-producer --broker-list localhost:9092 --topic test-topic

kafka-console-consumer --bootstrap-server localhost:9092 --topic test-topic --from-beginning



