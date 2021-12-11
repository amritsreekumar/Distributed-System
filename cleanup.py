from kafka import KafkaConsumer
from json import loads


subscribers = ["subscriber1", "subscriber2","subscriber3","subscriber4","subscriber5","subscriber6","subscriber7","subscriber8", "subscriber9", "subscriber10"]
subdict = {}
for i in subscribers:
    print(i)
    subdict[i] = KafkaConsumer(
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id=i,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for i in subscribers:
    print(subdict[i].topics())
    #subdict[i].unsubscribe()
