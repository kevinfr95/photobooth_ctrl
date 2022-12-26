
import RPi.GPIO as GPIO

light_intensity = 0

# Input 
btn_right  = 5
btn_left  = 6

# Output
light_right = 13
light_left = 12

	
# Init
GPIO.setmode(GPIO.BCM)
GPIO.setup(light_right, GPIO.OUT)
GPIO.setup(light_left, GPIO.OUT)

GPIO.setup(btn_right,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set
p_right = GPIO.PWM(light_right, 800)
p_right.start(light_intensity)

p_left = GPIO.PWM(light_left, 800)
p_left.start(light_intensity)


# Functions
def gpio_callback(channel):
    if channel == btn_left:
        light_intensity_update()
    elif channel == btn_right:
        print("Shutdown...")

def light_intensity_update():
    global light_intensity
    light_intensity = light_intensity + 20
    print("Change light intensity to %s %", light_intensity)

    if light_intensity > 100:
        light_intensity = 0
    
    p_right.ChangeDutyCycle(light_intensity)
    p_left.ChangeDutyCycle(light_intensity)


# Set Events
GPIO.add_event_detect(btn_right, GPIO.FALLING, callback=gpio_callback, bouncetime=500)
GPIO.add_event_detect(btn_left, GPIO.FALLING, callback=gpio_callback, bouncetime=500)



input('Type "Enter" to exit...')
p_right.stop()
p_left.stop()

GPIO.cleanup()
