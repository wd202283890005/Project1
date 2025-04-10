# reaction_step4.py
from gpiozero import LED, Button
from time import sleep
from random import uniform

# Hardware setup
led = LED(4)
left_button = Button(14)
right_button = Button(15)

def button_pressed(btn):
    print(f"Button on GPIO{btn.pin.number} pressed!")

# Event handlers
left_button.when_pressed = button_pressed
right_button.when_pressed = button_pressed

try:
    print("Button detection test")
    while True:
        led.on()
        sleep(uniform(5, 10))
        led.off()
        sleep(1)  # Response window
except KeyboardInterrupt:
    led.off()
    print("\nTest terminated")