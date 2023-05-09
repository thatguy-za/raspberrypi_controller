import RPi.GPIO as GPIO
import time
import os

# Define the GPIO pins and blink time that you will use.

shutdown_pin = 2
restart_pin = 3
led_pin = 4
blink_time = 0.2

# Setup the pin to use internal pullup resistors and the operating mode (input/output).

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(shutdown_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(restart_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Defines the Shutdown and Restart functions that will be called when the buttons are pushed

def Shutdown(channel):
   for x in range(2):
      # Blinks the LED twice
      GPIO.output(led_pin,GPIO.HIGH)
      time.sleep(blink_time)
      GPIO.output(led_pin,GPIO.LOW)
      time.sleep(blink_time)
   time.sleep(1)
   os.system("date | tr '\n' '\t' >> /home/pi/log.txt && echo 'Shutting down' >> /home/pi/log.txt")
   os.system("sudo poweroff")

def Restart(channel):
   for x in range(3):
      # Blinks the LED three times
      GPIO.output(led_pin,GPIO.HIGH)
      time.sleep(blink_time)
      GPIO.output(led_pin,GPIO.LOW)
      time.sleep(blink_time)
   time.sleep(1)
   os.system("date | tr '\n' '\t' >> /home/pi/log.txt && echo 'Restarting' >> /home/pi/log.txt")
   os.system("sudo reboot")

# Add our function to execute when a button is pressed.
# I've set the bouncetime to 10 seconds so you can hold the button down while you wait for the LED's to blink

GPIO.add_event_detect(3, GPIO.FALLING, callback = Restart, bouncetime = 10000)
GPIO.add_event_detect(2, GPIO.FALLING, callback = Shutdown, bouncetime = 10000)

# Now wait!

while 1:
   time.sleep(1)
