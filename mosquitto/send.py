import paho.mqtt.client as mqtt
import time 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("CONNECTED!!")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")

Connected = False  # global variable for the state of the connection
client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)
client.loop_start()  # start the loop
while Connected != True:  # Wait for connection
    time.sleep(0.1)
try:
    while True:
        name="Blacko biom:"
        message= input('Your message: ')
        new_message=name+ message
        client.publish("Eljay", new_message)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()    
