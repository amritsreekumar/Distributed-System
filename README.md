# Distributed-System

This template used for front end: (https://colorlib.com)
This webapp is built using the python-flask framework with SQLite running in the back-end. 
The client interacts with the web UI to enter the information required to query about the climatic trends in different countries. 

The application is built around Apache-Kafka with a confluent-kafka docker image: https://github.com/wurstmeister/kafka-docker

To run the application:

To start the dockers, we have written a docker compose file, so that the 3 brokers and publisher and subscriber dockers starts with just one line of code


To build the docker

    docker-compose -f docker-compose.yml build

To compose the docker

    docker-compose -f docker-compose.yml up -d

Logging the consumer docker. Use this to see the published information for each consumer

  `docker logs consumer -f`

Example links:
        
        http://localhost:5001/publisher1 (Just one example for publisher1, it can be changed to publisher1-publisher3)
        
        http://localhost:5002/subscriber1 (Just one example for subscriber1, it can be changed to subscriber1-subscriber10)


Type in the country name and choose the required options as per the drop down.

Hit submit

Scroll down to find a button that says "display in terminal" to trigger the function that displays the received messages in the consumer log mentioned above.
