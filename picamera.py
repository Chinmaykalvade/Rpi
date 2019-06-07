# !/usr/bin/python
# load sudo modprobe bcm2835-v4l2  for video input
#Import dependencies from pygame, time, GPIO, sys and OS
import sys, os, pygame
import pygame.camera
import time
import datetime
import picamera
from picamera import PiCamera
import pygame.image
from time import sleep, strftime
import RPi.GPIO as GPIO 

# Set GPIO pins for camera button
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, GPIO.PUD_UP)
# GPIO 26 is the shutter button
button=26

GPIO.setup(21, GPIO.OUT)
# GPIO 16 is the infrared cathode
GPIO.setup(20, GPIO.OUT)
# GPIO 20 is the white light cathode
GPIO.output(21, True)
# Sets the infrared cathode to ground. The common anode of the 
# LED is set to 3.3 V, so setting GPIO 16 to ground causes the 
# infrared light to be on.
GPIO.output(20, False)
# Sets the white light cathode to 3.3 V

input_state=GPIO.input(button)

# Change display to tft screen
#os.environ["SDL_FBDEV"] = "/dev/fb1"

# Initialize pygame
pygame.init()

# Initialize camera
pygame.camera.init()

# Disable mouse pointer
# pygame.mouse.set_visible(False)

# Set screen size

screen = pygame.display.set_mode((0,0)FULLSCREEN)

# Set the camera to use, the resolution, and start it
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera('/dev/video0', (1024,720))
cam.start()

# Declare variables that will be used in the code
# dropbox_token = '[place your token here]'
# local_dst = '/home/pi/Pictures'
# dropbox_dst = '/'
# upload_trigger = 0

# Define the 'takePicture' function that will:
# 1. Capture the image from the camera
# 2. Create a date variable and save picture using the date
# 3. Set the screen to black
# 4. Render text saying 'Picture Captured'
# 5. Rotate the text to match the screen orientation
# 6. Put contents on the screen (with screen.blit)
# 7. Refresh the screen using 'screen.flip'
#8. Pause for 2 secs, and then load the saved picture
# 9. Adjust the size and orientation and display it to the screen using screen.blit
def takePicture():
    snapshot = cam.get_image()
    curr_time =(time.strftime("%y-%b-%d_%H:%M:%S"))
    pygame.image.save(snapshot,"/home/pi/Pictures/funduscam%s.jpg" %(curr_time))
    screen.fill((0,0,0,0))
    pygame.display.update()
    font = pygame.font.Font(None, 25)
    text = font.render("Picture Captured", 0, (0, 250, 250))
    Surf = pygame.transform.rotate(text, -270)
    screen.blit(Surf, (50, 10))
    pygame.display.flip()
    sleep(2)
    preview= pygame.image.load("/home/pi/Pictures/cam%s.jpg"% (curr_time))
    preview = pygame.transform.scale(preview, (720, 720))
    preview2 = pygame.transform.rotate(preview, 90)
    screen.blit(preview2, (0, 0))
    pygame.display.flip()
    GPIO.output(21, False)
    GPIO.output(20, True)

def main()
# Start the main loop
while True:
    # Continuously capture images from the camera, 
    # adjust them, and display them
    image1 = cam.get_image()
    image1 = pygame.transform.scale(image1, (1280, 720))
    image2 = pygame.transform.rotate(image1, 90)
    screen.blit(image2, (0, 0))
    pygame.display.update()
    # Check to see if the GPIO button is triggered. If so, then:
    # 1. Run the 'take picture' function
    # 2. Refresh the screen and set the upload variable to 1.
    if (GPIO.input(26) == False):
        takePicture()
        sleep(1)
        GPIO.cleanup()
    # For any error, stop the camera, quit pygame, and exit the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cam.stop()
                pygame.quit()
                sys.exit()


