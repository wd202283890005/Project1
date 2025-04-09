# reaction_step2.py
from gpiozero import LED
from time import sleep

# Initialize LED on GPIO4
led = LED(4)

try:
    print("Testing LED control...")
    while True:
        led.on()
        print("LED ON")
        sleep(2)
        led.off()
        print("LED OFF")
        sleep(2)
except KeyboardInterrupt:
    led.off()
    print("\nTest terminated")