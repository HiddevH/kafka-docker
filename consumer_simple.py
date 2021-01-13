from kafka import KafkaConsumer
from json import loads
from time import sleep

consumer = KafkaConsumer(
    'test_message',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
     value_deserializer=lambda m: loads(m.decode('utf-8')),
    )


for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)