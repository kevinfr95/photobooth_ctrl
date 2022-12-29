import RPi.GPIO as GPIO
import os
import time
from gpiozero import CPUTemperature
import asyncio

light_on = False
cpu = CPUTemperature()

# Input 
btn_right  = 5
btn_left  = 6

# Output
light_right = 13
light_left = 12



def setup():  
    # Init
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(light_right, GPIO.OUT)
    GPIO.setup(light_left, GPIO.OUT)

    GPIO.setup(btn_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Set
    GPIO.output(light_left, light_on)
    GPIO.output(light_right, light_on)
    
    # Set Events
    GPIO.add_event_detect(btn_right, GPIO.RISING, callback=gpio_callback, bouncetime=400)
    GPIO.add_event_detect(btn_left, GPIO.FALLING, callback=gpio_callback, bouncetime=400)


# Functions
def gpio_callback(channel):
    if channel == btn_left:
        light_update()
    elif channel == btn_right:
       asyncio.run(shutdown_system())


async def shutdown_system():
    time.sleep(2)
    if GPIO.input(btn_right) == 0:
        print("Shutdown...")
        os.system("systemctl poweroff")

def light_update():
    global light_on
    light_on = not light_on

    print("Light", "on" if light_on else "off" )
    GPIO.output(light_left, light_on)
    GPIO.output(light_right, light_on)


    

if __name__ == '__main__':

    print("Initialization...")
    setup()

    print("Process started")
    
    while 1:
        print("CPU Temperature:", cpu.temperature)
        time.sleep(120)


