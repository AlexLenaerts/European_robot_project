
import RPi.GPIO as GPIO  # Import the GPIO Library
import time  # Import the Time library

import move
import detection

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Your code to control the robot goes below this line
try:
    # Set trigger to False (Low)
    GPIO.output(pinTrigger, False)

    # Allow module to settle
    time.sleep(0.1)

    # repeat the next indented block forever
    while True:
        forwards()
        time.sleep(0.1)
        if isnearobstacle(hownear,pinTrigger_F,pinEcho_F):
            stopmotors()
            avoidobstacle()

# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    GPIO.cleanup()