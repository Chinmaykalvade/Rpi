##this one uses button at in pin 19, please add required button to the gpio board.
##Program should technically work as long as button stays on. And program should turn off when button does.
import io
import picamera
from time import sleep
import time
import RPi.GPIO as GPIO
from os import system
import os
import random, string

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button = 19 #Button GPIO Pin

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
led_1 = 12 #Status LED GPIO Pin
GPIO.setup(led_1, GPIO.OUT)
led_2 = 21 #ON/OFF LED Pin
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
# GPIO 22 is the infrared cathode
GPIO.setup(23, GPIO.OUT)
# GPIO 23 is the white light cathode
GPIO.output(22, False)
# Sets the infrared cathode to ground. The common anode of the 
# LED is set to 3.3 V, so setting GPIO 22 to ground causes the 
# infrared light to be on.
GPIO.output(23, True)
# Sets the white light cathode to 3.3 V

flash = 13# add flash required flash ( white/ infrared) to this pin.
GPIO.setup(flash, GPIO.OUT)


########################
### Variables Config ###
########################

camera = picamera.PiCamera()
camera.resolution = (540, 405)
camera.rotation = 90
#camera.brightness = 70
camera.image_effect = 'none'
GPIO.output(led_2, 1)
print('System Ready')

def random_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

while True:
    input_state = GPIO.input(button) # Sense the button
    randomstring = random_generator()
    if input_state == False:	
	GPIO.output(flash,1)
        GPIO.output(led_1,1)
        # Explicitly open a new file called my_image.jpg
        my_file = open('/home/pi/picamera/cam/' + randomstring + '-0', 'wb')
        with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(my_file)
        # At this point my_file.flush() has been called, but the file has
        # not yet been closed
        GPIO.output(flash,0)
        
        GPIO.output(led_1,0)
    	graphicsmagick = "gm convert -delay " + str(gif_delay) + " " + "*.jpg " 
        os.system(graphicsmagick)
        print('Done')
        print('System Ready')
    else :
        # Switch on LED
        GPIO.output(led_1, 1)
        time.sleep(0.35)
        GPIO.output(led_1, 0)
        time.sleep(0.35)


        

       
        
