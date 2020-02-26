from sense_hat import SenseHat
from time import sleep
from random import randint

#init
sense = SenseHat()
sense.set_imu_config(False, False, False)


# Generate a random colour
def pick_random_colour():
  
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)
  

def main():
    while True:
      print(pick_random_colour())
      sense.show_letter("N", text_colour=pick_random_colour())
      sleep(1)
      sense.show_letter("M", text_colour=pick_random_colour())
      sleep(1)
      sense.show_letter("D", text_colour=pick_random_colour())
      print('test')
      sleep(1)

      
try:
  main()
except (KeyboardInterrupt, SystemExit):
  print('Programma sluiten')
  sense.clear()