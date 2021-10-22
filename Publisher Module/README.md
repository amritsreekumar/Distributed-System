# Distributed-System

This template used for front end: (https://colorlib.com)
This webapp is built using the python-flask framework with SQLite running in the back-end.
The client interacts with the web UI to enter the information required to query about the climatic trends in different countries. This search query is also stored in the persistent database that does not get lost once the server restarts.

To run the application:

Change to the working directory

docker build -t flaskapp:latest .

docker run -it -d -p 5001:5001 flaskapp

Log on to 127.0.0.1:5001/

Type in the country name and choose the required options as per the drop down.

Hit submit

Scroll down to find the previously queried searches and it will have the searches stored in the database. Alternatively, go to Log on to 127.0.0.1:5000/display to find the previous queries and database.
