import time
import RPi.GPIO as GPIO
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
while True:
  #take a reading
  input = GPIO.input(18)
  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed")
  #update previous input
  prev_input = input
  #slight pause to debounce
  time.sleep(0.05)