import paho.mqtt.client as mqtt
import time
def  on_connect(client, userdata, flags,rc):
    print("connected with result code" + str(rc))
    client.subscribe("Eljay")
def on_message(client,userdata,msg):
    print(msg.topic+"\n" +msg.payload.decode("utf-8")+"\n")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.emqx.io", 1883, 60)
client.loop_forever()
