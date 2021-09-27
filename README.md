# Distributed-System

This template used for front end: (https://colorlib.com)

Instructions to run web page locally:

cd Distributed-System

To run the application:

Change to the working directory

docker build -t flaskapp:latest .

docker run -it -d -p 5000:5000 flaskapp

Log on to 127.0.0.1:5000/

Type in the country name and choose the required options as per the drop down.

Hit submit

Scroll down to find the previously queried searches and it will have the searches stored in the database. Alternatively, go to Log on to 127.0.0.1:5000/display to find the previous queries and database.