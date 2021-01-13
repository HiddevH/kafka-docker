
from kafka import KafkaProducer
import protobuf.addressbook_pb2 as ab 
import sys

# Initialize KafkaProducer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'])

address_book = ab.AddressBook()

# This function fills in a Person message based on user input.
def PromptForAddress(person):
  person.id = int(input("Enter person ID number: "))
  person.name = input("Enter name: ")

  email = input("Enter email address (blank for none): ")
  if email != "":
    person.email = email

  while True:
    number = input("Enter a phone number (or leave blank to finish): ")
    if number == "":
      break

    phone_number = person.phones.add()
    phone_number.number = number
    type = input("Is this a mobile, home, or work phone? ")
    if type == "mobile":
      phone_number.type = ab.Person.PhoneType.MOBILE
    elif type == "home":
      phone_number.type = ab.Person.PhoneType.HOME
    elif type == "work":
      phone_number.type = ab.Person.PhoneType.WORK
    else:
      print("Unknown phone type; leaving as default value.")
    return person

while True:
    #new_person = ab.Person()
    PromptForAddress(address_book.people.add())
    producer.send('addressbook', value=address_book.SerializeToString())
    add_new_person = input("Do you want to add a new person? Leave blank to stop: ")
    if add_new_person == "":
        break