#This script uses the gpiozero library to shut down a pi. Depending on your distro, you might need to run the poweroff command as sudo.
from gpiozero import Button
import time
import os

# The pi will shutdown when pin 21 is connected to ground
shutdown_button_pin = Button(21, pull_up=True)

while True:
     if shutdown_button_pin.is_pressed:
        time.sleep(2)
        # wbutton must be pressed for 2 seconds
        if shut_But.is_pressed:
            os.system("poweroff")
            time.sleep(1)
