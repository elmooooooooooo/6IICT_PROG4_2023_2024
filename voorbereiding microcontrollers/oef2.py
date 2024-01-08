from gpiozero import LED
from time import sleep

# Define the GPIO pin numbers where your LEDs are connected
red_led = LED(17)    # Red LED connected to GPIO pin 17
yellow_led = LED(27) # Yellow LED connected to GPIO pin 27
green_led = LED(22)  # Green LED connected to GPIO pin 22

# Function to simulate a traffic light cycle
def traffic_light_cycle():
    # Red light (stop)
    red_led.on()
    yellow_led.off()
    green_led.off()
    sleep(3)

    # Red and yellow lights (prepare to go)
    red_led.on()
    yellow_led.on()
    green_led.off()
    sleep(1)

    # Green light (go)
    red_led.off()
    yellow_led.off()
    green_led.on()
    sleep(3)

    # Yellow light (prepare to stop)
    red_led.off()
    yellow_led.on()
    green_led.off()
    sleep(1)

# Main program
if __name__ == "__main__":
    try:
        while True:
            traffic_light_cycle()

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, cleanup and exit
        red_led.off()
        yellow_led.off()
        green_led.off()
        print("Program terminated by user.")
