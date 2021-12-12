# Distributed-System

This template used for front end: (https://colorlib.com)
This webapp is built using the python-flask framework with SQLite running in the back-end. 
The client interacts with the web UI to enter the information required to query about the climatic trends in different countries. 
This search query is also stored in the persistent database that does not get lost once the server restarts.

To run the application:

In order for the brokers to share the same db, we have made use of docker volume and its, attached with just the brokers.


To build the docker

    docker-compose build

To compose the docker

    docker-compose -f docker-compose.yml up -d

To see the logs
  
    docker-compose logs -f 

To see the kafka docker

    docker exec -it kafka /bin/bash
    cd opt/kafka/bin
    ./kafka-topics.sh --bootstrap-server kafka:9092 --create --topic USA --partitions 2 --replication-factor 4
    ./kafka-topics.sh --bootstrap-server kafka:9092 --create --topic MEX --partitions 1 --replication-factor 4
    ./kafka-topics.sh --bootstrap-server kafka:9092 --create --topic CAN --partitions 1 --replication-factor 4

List the topics

    ./kafka-topics.sh --bootstrap-server kafka:9092 --list

Example links:
        
        http://localhost:5001/publisher1 (Just one example for publisher1, it can be changed to publisher1-publisher12)
        
        http://localhost:5002/subscriber1 (Just one example for subscriber1, it can be changed to subscriber1-subscriber12)


Type in the country name and choose the required options as per the drop down.

Hit submit

Scroll down to find the previously queried searches and it will have the searches stored in the database along with the published data as per the subscription. 

