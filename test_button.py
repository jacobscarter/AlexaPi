import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

while True:
  while GPIO.input(18)==0:
      print('The Button Was Pressed!')