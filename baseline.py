from sense_hat import SenseHat
from time import sleep
from random import randint

#Init
sense = SenseHat()
sense.set_imu_config(False, False, False)


# Generate a random colour
def pick_random_colour():
  
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)
  
# Display Msg
def main():
    while True:
      sense.show_message("Hello!", text_colour=pick_random_colour(), back_colour=pick_random_colour())


      
try:
  main()
except (KeyboardInterrupt, SystemExit):
  print('Programma sluiten')
  sense.clear()