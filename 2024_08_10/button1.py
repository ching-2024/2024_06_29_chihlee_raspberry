import signal
from gpiozero import Button,LED
from datetime import datetime

def user_release():
    print('user release button')
    led.toggle()
    now = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')
    print(now_str)

    if led.is_lit:
        print('light on')
    else:
        print('light off')

if __name__ == '__main__':
    button = Button(pin=18)
    button.when_released = user_release
    led = LED(pin=25)
    #休眠直到收到信號，自已調用適當的處理程序
    signal.pause() 
    

