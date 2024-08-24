import signal
from gpiozero import Button,LED
from datetime import datetime
import paho.mqtt.publish as publish
import os
from dotenv import load_dotenv
load_dotenv() #載入.env的

def user_release():
    print('user release button')
    led.toggle()
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str)
    if led.is_lit:
        message = f'''{{
            "status":"true",
            "date":"{now_str}",
            "topic":"501classroom" 
        }}'''
    else:
        message = f'''{{
            "status":"false",
            "date":"{now_str}",
            "topic":"501classroom" 
        }}'''
    #end if led.is_lit:
    #message = str(data)  #mqtt只收字串
    print(message)
    publish.single(topic='501classroom', payload=message, hostname='127.0.0.1', qos=2, auth={'username':os.environ['MQTT_USERNAME'], 'password':os.environ['MQTT_PASSWORD']})


if __name__ == '__main__':
    button = Button(pin=18)
    button.when_released = user_release
    led = LED(pin=25)
    #休眠直到收到信號，自已調用適當的處理程序
    signal.pause() 
    

