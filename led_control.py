import RPi.GPIO as GPIO
import time

class LedControl:
  def __init__(self, pin, warnings = False):
    self.pin = pin
    self.warnings = warnings

  def setup(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(self.warnings)
    GPIO.setup(self.pin, GPIO.OUT)

  def on(self):
    print("LED on")
    GPIO.output(self.pin, GPIO.HIGH)

  def off(self):
    print("LED off")
    GPIO.output(self.pin, GPIO.LOW)

  def toggle(self):
    status = GPIO.input(self.pin)
    if status == GPIO.LOW:
    	self.on()
    else:
    	self.off()
