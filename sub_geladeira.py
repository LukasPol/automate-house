import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from time import sleep
from json import loads
import configparser
from playsound import playsound


def on_message(client, userdate, message):
    dados = loads(str(message.payload.decode()))
    status = dados["field1"]
    if int(status) == 1:
        playsound('song.mp3')
        sleep(5)


config = configparser.ConfigParser()
config.read("conf")

broker = config["DEFAULT"]["BROKER"]
port = int(config["DEFAULT"]["PORT"])
topic = config["THINGSPEAK"]["TOPIC_SUBSCRIBE"]
username = config["THINGSPEAK"]["USERNAME"]
password = config["THINGSPEAK"]["MQTT_API_KEY"]

subscribe.callback(
    on_message,
    qos=0,
    topics=topic,
    hostname=broker,
    port=port,
    client_id="clisub",
    auth={"username": username, "password": password},
)

# while True:
#     sleep(20)