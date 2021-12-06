from time import sleep
from json import dumps
from kafka import KafkaProducer

topics = ["a","b"]
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
                         

for e in range(100):
    data = {'number' : e}
    producer.send('a', value=data)
    sleep(5)


