# Distributed-System

This template used: (https://colorlib.com)

Instructions to run web page locally:

pip3 install flask

cd Distributed-System

export FLASK_APP=app

export FLASK_ENV=development

flask run

Open http://127.0.0.1:5000/ on your browser

http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1920/1939/IND.csv
sample api call

To run the application:

docker build -t flaskapp:latest .

docker run -it -d -p 5000:5000 flaskapp

Log on to 127.0.0.1:5000/

Type in the country name and choose the required options.

Hit submit

Scroll down to find the previously queried searches