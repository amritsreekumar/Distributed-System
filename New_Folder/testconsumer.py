from kafka import KafkaConsumer
from json import loads

subscribers = ["subscriber1", "subscriber2","subscriber3","subscriber4","subscriber5","subscriber6","subscriber7","subscriber8" "subscriber9", "subscriber10"]

# subs = ["sub1", "sub2"]
# consumer = KafkaConsumer(
#      bootstrap_servers=['localhost:9092'],
#      auto_offset_reset='earliest',
#      enable_auto_commit=True,
#      value_deserializer=lambda x: loads(x.decode('utf-8')))

# consumer2 = KafkaConsumer(
#      bootstrap_servers=['localhost:9092'],
#      auto_offset_reset='earliest',
#      enable_auto_commit=True,
#      value_deserializer=lambda x: loads(x.decode('utf-8')))


# consumer.subscribe('b')
# consumer2.subscribe('a')


# for message in consumer:
#     print(message)
#     message = message.value
#     print(message)


subdict = {}
for i in subscribers:
    subdict[i] = KafkaConsumer(
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

subdict['subscriber1'].subscribe(['Ass_tas'])
subdict['subscriber1'].subscribe(['USA_tas'])
subdict['subscriber1'].subscribe('MEX_tas')
print(subdict['subscriber1'].topics())
for msg in subdict['subscriber1']:
    print(msg.value)