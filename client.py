from random import randint
from time import sleep
from datetime import datetime
from json import dumps
from os import environ
import paho.mqtt.publish as publish

# getting environment variables
BROKER = environ.get('RABBITMQ_HOST')
TOPIC = environ.get('MQTT_TOPIC')

# publishing random status messages to the specified topic every second
while True:
    status = randint(0, 6)
    message = dumps({"status": status, "timestamp": datetime.now().isoformat()})
    publish.single(TOPIC, message, hostname=BROKER)
    print(f"Message {message} sent to topic {TOPIC}.")
    sleep(1)
