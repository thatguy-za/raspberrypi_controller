from gpiozero import Button
from signal import pause
import os

# The pi will shutdown when pin 21 is connected to ground for 2 seconds
shutdown_button_pin = Button(21, hold_time=2)

def shutdown():
    os.system("poweroff")

shutdown_button_pin.when_held = shutdown

pause()
