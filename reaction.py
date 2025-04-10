# reaction_step3.py
from gpiozero import LED
from time import sleep
from random import uniform

led = LED(4)

try:
    print("Random interval test")
    while True:
        delay = uniform(5, 10)
        led.on()
        print(f"LED ON for {delay:.2f} seconds")
        sleep(delay)
        led.off()
        print("LED OFF")
        sleep(1)  # Brief pause between cycles
except KeyboardInterrupt:
    led.off()
    print("\nTest terminated")