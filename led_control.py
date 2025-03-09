import RPi.GPIO as GPIO
import time

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

def on():
    print("LED on")
    GPIO.output(LED_PIN, GPIO.HIGH)

def off():
    print("LED off")
    GPIO.output(LED_PIN, GPIO.LOW)

def toggle():
    status = GPIO.input(LED_PIN)
    if status == GPIO.LOW:
        on()
    else:
        off()
