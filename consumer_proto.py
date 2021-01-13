from kafka import KafkaConsumer
from json import loads
from time import sleep
from google.protobuf.json_format import MessageToDict

consumer = KafkaConsumer(
    'addressbook',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id'
    )

import protobuf.addressbook_pb2 as ab 

address_book = ab.AddressBook()

for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    address_book.ParseFromString(event_data)
    print('Caught a new address!: ')
    print(address_book)
    dict_msg = MessageToDict(address_book)
    print('dict: ')
    print(dict_msg)