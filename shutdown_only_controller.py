from gpiozero import Button
from signal import pause

# The pi will shutdown when pin 21 is connected to ground
shutdown_button_pin = Button(21, hold_time=2)

def shutdown():
    check_call(['poweroff'])

shutdown_button_pin.when_held = shutdown

pause()
