import paho.mqtt.client as mqtt
import time
from colorama import init, Fore

init()

def on_connect(client, userdata, flags, rc):
    client.subscribe("glblcd")

def on_message(client, userdata, msg):
    print(msg.topic +" :"+ msg.payload.decode("utf-8") + "\n")

def send_message(client, topic, message):
    client.publish(topic, message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.emqx.io",1883,60)
client.loop_forever()  

while True:
    message = input("Enter message to send: ")
    send_message(client, "glblcd", Fore.BLUE + message + Fore.RESET)

