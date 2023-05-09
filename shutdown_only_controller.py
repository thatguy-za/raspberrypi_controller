import RPi.GPIO as GPIO
import os

# Define the GPIO pins and blink time that you will use.

shutdown_pin = 21

# Setup the pin to use internal pullup resistors and the operating mode (input/output).

GPIO.setmode(GPIO.BCM)
GPIO.setup(shutdown_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Defines the Shutdown and Restart functions that will be called when the buttons are pushed

def Shutdown(channel):
   os.system("sudo poweroff")

# Add our function to execute when a button is pressed.
# I've set the bouncetime to 10 seconds so you can hold the button down while you wait for the LED's to blink

GPIO.add_event_detect(2, GPIO.FALLING, callback = Shutdown, bouncetime = 10000)

# Now wait!

while 1:
   time.sleep(1)
