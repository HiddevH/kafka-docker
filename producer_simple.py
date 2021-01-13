
from kafka import KafkaProducer
import sys
from json import dumps

# Initialize KafkaProducer
producer = KafkaProducer(
     value_serializer=lambda m: dumps(m).encode('utf-8'), 
      bootstrap_servers=['localhost:9092'])


# This function requests a message:
def draft_msg():
  subject = input('Please provide the subject of your message: ')
  message = input('What is your message?: ')

  return {subject : message}

while True:
    msg = draft_msg()
    producer.send('test_message', value=msg)
    add_new_person = input("Do you want to add a new message? Leave blank to stop: ")
    if add_new_person == "":
        break