from time import sleep
from json import dumps
from kafka import KafkaProducer

topics = ["a","b"]
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
                         


data = 'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1960/1979/USA'
producer.send('a', value=data)
sleep(2)
print("lolz")


