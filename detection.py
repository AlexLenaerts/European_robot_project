#import RPi.GPIO as GPIO  # Import the GPIO Library
#import time  # Import the Time library

from move import *

#BACK
pinTrigger_B = 27
pinEcho_B = 4

#LEFT
pinTrigger_L = 17
pinEcho_L = 18

#FRONT
pinTrigger_F = 22
pinEcho_F = 23

#RIGHT
pinTrigger_R = 24
pinEcho_R = 25

# Set pins as output and input
GPIO.setup(pinTrigger_B, GPIO.OUT)  # Trigger
GPIO.setup(pinEcho_B, GPIO.IN)  # Echo
GPIO.setup(pinTrigger_L, GPIO.OUT)  # Trigger
GPIO.setup(pinEcho_L, GPIO.IN)  # Echo
GPIO.setup(pinTrigger_R, GPIO.OUT)  # Trigger
GPIO.setup(pinEcho_R, GPIO.IN)  # Echo
GPIO.setup(pinTrigger_F, GPIO.OUT)  # Trigger
GPIO.setup(pinEcho_F, GPIO.IN)  # Echo


# Distance Variables
hownear = 20.0
reversetime = 0.5
turntime = 0.75


# Take a distance measurement
def measure(pinTrigger,pinEcho):
    GPIO.output(pinTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)
    starttime = time.time()
    stoptime = starttime

    while GPIO.input(pinEcho) == 0:
        starttime = time.time()
        stoptime = starttime

    while GPIO.input(pinEcho) == 1:
        stoptime = time.time()
        # If the sensor is too close to an object, the Pi cannot
        # see the echo quickly enough, so we have to detect that
        # problem and say what has happened.
        if stoptime - starttime >= 0.04:
            print("Hold on there!  You're too close for me to see.")
            stoptime = starttime
            break

    elapsedtime = stoptime - starttime
    distance = (elapsedtime * 34300) / 2

    return distance


# Return True if the ultrasonic sensor sees an obstacle
def isnearobstacle(localhownear,pinTrigger,pinEcho):
    distance = measure(pinTrigger,pinEcho)

    print(pinTrigger,"IsNearObstacle: " + str(distance))
    if distance < localhownear:
        return True
#	print("IsNearObstacle: " + str(distance))
    else:
        return False


# Move back a little, then turn right
def avoidobstacle():
    compteur = 0
    # Back off a little
    print("stop")
    stopmotors()
    if (isnearobstacle(hownear,pinTrigger_B,pinEcho_B)==False):
       print("Backwards")
       backwards()
       time.sleep(reversetime)
       stopmotors()
    else:
       stopmotors()

    #gauche ou droite ?

    if ((isnearobstacle(hownear,pinTrigger_L,pinEcho_L)==True) and (isnearobstacle(hownear,pinTrigger_R,pinEcho_R)==False)):
       print("Right")
       right()
       time.sleep(turntime)
       stopmotors()

    elif ((isnearobstacle(hownear,pinTrigger_R,pinEcho_R)==True) and (isnearobstacle(hownear,pinTrigger_L,pinEcho_L)==False)):
       print("Left")
       left()
       time.sleep(turntime)
       stopmotors()
    elif ((isnearobstacle(hownear,pinTrigger_R,pinEcho_R)==False) and (isnearobstacle(hownear,pinTrigger_L,pinEcho_L)==False)):
         print("Right2")
         right()
         time.sleep(turntime)
         stopmotors()
#        else :
   # if (isnearobstacle(hownear,pinTrigger_B,pinEcho_B)==False):
    #		print("Back!")
    #		backwards()
    #		time.sleep(10)
    #		stopmotors()
#    	else: 
 #   		stopmotors()


