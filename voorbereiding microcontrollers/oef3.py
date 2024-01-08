from gpiozero import LED, Device
from signal import pause

# Set the blink rate globally
Device.pin_factory.blink_rate = 1

# Define the GPIO pin numbers where your LEDs are connected
led1 = LED(17)  # Change the pin number as per your connection
led2 = LED(18)  # Change the pin number as per your connection

# Blink function to make the LED blink
def custom_blink(led, blink_count=5):
    led.blink(on_time=0.5, off_time=0.5, n=blink_count)

# Main program
if __name__ == "__main__":
    try:
        # Blink the first LED
        custom_blink(led1)

        # Blink the second LED
        custom_blink(led2)

        # Keep the program running
        pause()

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, cleanup and exit
        led1.off()
        led2.off()
        print("Program terminated by user.")
