import RPi.GPIO as GPIO
from detection import *
from move import*
import sys
from threading import Thread
from picamera import PiCamera
from pistreaming.server import *


class Robot(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.Terminated = False

    def run(self):
        # Set trigger to False (Low)
        GPIO.output(pinTrigger_B, False)
        GPIO.output(pinTrigger_F, False)
        GPIO.output(pinTrigger_R, False)
        GPIO.output(pinTrigger_L, False)
        # Allow module to settle
        sleep(0.1)
        while not self.Terminated:
            forwards()
            print("forward")
            sleep(0.1)
            if isnearobstacle(hownear, pinTrigger_F, pinEcho_F):
                print("stop123")
               # stopmotors()
                avoidobstacle()
        stopmotors()
        print("stop robot")
        GPIO.cleanup()

    def stop(self):
        self.Terminated = True


class Camera(Thread):

   # Thread charge simplement afficher une lettre dans la console

    def __init__(self):
        Thread.__init__(self)

    def run(self):
      #     while not self.Terminated:
        main()


def maint():
    t1 = Robot()
    t2 = Camera()
    try:
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except KeyboardInterrupt:
        t1.stop()


if __name__ == '__main__':

    maint()
