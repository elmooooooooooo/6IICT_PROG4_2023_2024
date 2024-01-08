from gpiozero import LED
from time import sleep

# Define the GPIO pin numbers where your LEDs are connected
led1 = LED(17)  # Change the pin number as per your connection
led2 = LED(18)  # Change the pin number as per your connection

# Blink function to make the LED blink
def blink(led, duration, blink_count=5):
    for _ in range(blink_count):
        led.on()
        sleep(duration)
        led.off()
        sleep(duration)

# Main program
if __name__ == "__main__":
    try:
        # Blink the first LED
        blink(led1, 0.5)

        # Blink the second LED
        blink(led2, 0.3)

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, cleanup and exit
        led1.off()
        led2.off()
        print("Program terminated by user.")
