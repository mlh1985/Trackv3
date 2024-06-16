import RPi.GPIO as GPIO
from time import sleep
#GPIO
GPIO.setmode(GPIO.BCM)

#Pin definitions
start_button_pin = 18
finish_line_pins = [23,24,25,8,7] #Adjust according to your setup
actuator_pin = 17

#Setup pins
GPIO.setup(start_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
for pin in finish_line_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(actuator_pin, GPIO.OUT)

def start_race():
    GPIO.output(actuator_pin, GPIO.HIGH)
    sleep(1) # Adjust time as necessary to release cars
    GPIO.output(actuator_pin, GPIO.LOW)
    
def read_finish_line():
    results = []
    for pin in finish_line_pins:
        if GPIO.input(pin) == GPIO.LOW:
            results.append(pin)
    return results

def cleanup():
    GPIO.cleanup()