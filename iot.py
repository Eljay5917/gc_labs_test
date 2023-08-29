import requests
from gpiozero import Button
from signal import pause
def get_url():
    url = "https://maker.ifttt.com/trigger/button/json/with/key/gMvbMl2uPHAXFU_0WcPXZBvDviNofJYXc09UqEdabtg"
    r= requests.get(url)
    print(r.status_code)

 
button= Button(2)


while True:
    button.when_pressed=get_url()
    pause()