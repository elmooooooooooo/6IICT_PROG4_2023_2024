from gpiozero import LED
from time import sleep

# Define the GPIO pin numbers where your LEDs are connected
car_red_led = LED(17)      # Car red LED connected to GPIO pin 17
car_yellow_led = LED(27)   # Car yellow LED connected to GPIO pin 27
car_green_led = LED(22)    # Car green LED connected to GPIO pin 22

pedestrian_red_led = LED(5)     # Pedestrian red LED connected to GPIO pin 5
pedestrian_green_led = LED(6)   # Pedestrian green LED connected to GPIO pin 6

# Function to simulate a traffic light cycle for cars
def car_traffic_light_cycle():
    # Car red light (stop)
    car_red_led.on()
    car_yellow_led.off()
    car_green_led.off()
    sleep(3)

    # Car red and yellow lights (prepare to go)
    car_red_led.on()
    car_yellow_led.on()
    car_green_led.off()
    sleep(1)

    # Car green light (go)
    car_red_led.off()
    car_yellow_led.off()
    car_green_led.on()
    sleep(3)

    # Car yellow light (prepare to stop)
    car_red_led.off()
    car_yellow_led.on()
    car_green_led.off()
    sleep(1)

# Function to simulate a traffic light cycle for pedestrians
def pedestrian_traffic_light_cycle():
    # Pedestrian red light (stop)
    pedestrian_red_led.on()
    pedestrian_green_led.off()
    sleep(2)

    # Pedestrian green light (walk)
    pedestrian_red_led.off()
    pedestrian_green_led.on()
    sleep(5)

    # Pedestrian red light (stop)
    pedestrian_red_led.on()
    pedestrian_green_led.off()
    sleep(2)

# Main program
if __name__ == "__main__":
    try:
        while True:
            car_traffic_light_cycle()
            pedestrian_traffic_light_cycle()

    except KeyboardInterrupt:
        # If Ctrl+C is pressed, cleanup and exit
        car_red_led.off()
        car_yellow_led.off()
        car_green_led.off()
        pedestrian_red_led.off()
        pedestrian_green_led.off()
        print("Program terminated by user.")
