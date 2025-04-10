# reaction_step5.py
from gpiozero import LED, Button
from time import sleep
from random import uniform

# Hardware setup
led = LED(4)
left_button = Button(14)
right_button = Button(15)

# Get player names
left_name = input("Enter left player's name: ")
right_name = input("Enter right player's name: ")

def pressed(btn):
    winner = left_name if btn.pin.number == 14 else right_name
    print(f"{winner} won the game!")
    exit()

# Event handlers
left_button.when_pressed = pressed
right_button.when_pressed = pressed

try:
    print("Starting game...")
    led.on()
    sleep(uniform(5, 10))
    led.off()
    while True:  # Keep running until button press
        sleep(0.1)
except KeyboardInterrupt:
    led.off()
    print("\nGame terminated")