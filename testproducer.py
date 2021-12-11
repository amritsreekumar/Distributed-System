from time import sleep
from json import dumps
from kafka import KafkaProducer

topics = ["a","b"]
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
                         


data = 'USA'
data2 = 'MEX'
for i in range(100):
    producer.send('USA_tas', value=data)
    sleep(2)
    producer.send('MEX_tas', value=data2)
    sleep(2)
print("lolz")



