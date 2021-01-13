Kafka cluster in Docker
===
Run a local kafka cluster, including python scripts (JSON/Protobuf) to interact with them.

## Prerequisites
- Docker
- Docker-compose
- Python 3.8

## Instructions
Install Protobuf Compiler, for OSX you can use Homebrew: 

`brew install protobuf`


create and launch virtual environment:

`python -m venv .venv`

`source .venv/bin/activate`


install dependencies:

`pip install -r requirements.txt`


### Docker-compose:
`docker-compose -f docker-compose-yml up`

Wait a few minutes for everything to download, install and get up and running.

## Usage
Below are instrucitons on using the python scripts
### Simple (JSON)
Use the `producer_simple` and `consumer_simple` python scripts to interact with the kafka cluster using basic JSON messages. 

Example:

`python producer_simple.py`

```
Please provide the subject of your message: Hello
What is your message?: World
```

`python consumer_simple.py` 
output:

```json
{'Hello': 'World'}
```

### Protobuf
Use the `producer_proto` and `consumer_proto` python scripts to interact with the kafka cluster using Protobuf messages, example protobuf schema's are included to get up and running quickly.

Example:

`python producer_proto.py`

```
Enter person ID number: 1337
Enter name: Hidde
Enter email address (blank for none): hello@world.com
Enter a phone number (or leave blank to finish): 0001234567
Is this a mobile, home, or work phone? mobile
```

`python consumer_proto.py` 
output:

```
Caught a new address!: 
people {
  name: "Hidde"
  id: 1337
  email: "hello@world.com"
  phones {
    number: "0001234567"
    type: MOBILE
  }
}

dict:
{'people': [{'name': 'Hidde', 'id': 1337, 'email': 'hello@world.com', 'phones': [{'number': '0001234567', 'type': 'MOBILE'}]}]}
```

## Cleaning up
`docker-compose -f docker-compose.yml down -v`
note: -v removes volumes containing data
