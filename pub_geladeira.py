import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from time import sleep
from random import randint
import configparser

config = configparser.ConfigParser()
config.read("conf")

status_geladeira = ["abriu", "fechada"]

broker = config["DEFAULT"]["BROKER"]
port = int(config["DEFAULT"]["PORT"])
topic = config["THINGSPEAK"]["TOPIC_PUBLISH"]

while True:
    status = randint(0, 1)
    print(status)

    if status == 1:
        payload = f"field1={status}&status=MQTTPUBLISH"
        publish.single(payload=payload, topic=topic, port=port, hostname=broker)
        print(payload)
    sleep(20)
