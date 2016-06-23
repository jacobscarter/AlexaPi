import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
buttonPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin,GPIO.IN)

while True:
  #assuming the script to call is long enough we can ignore bouncing
  if (GPIO.input(buttonPin)):
    #this is the script that will be called (as root)
    print("Button Pressed")