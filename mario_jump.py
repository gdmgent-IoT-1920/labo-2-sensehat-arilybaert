from sense_hat import SenseHat
#import turtle
from time import sleep
from random import randint

screen = turtle.Screen()
#init
sense = SenseHat()
sense.set_imu_config(False, False, False)


# Or, set the shape of a turtle
screen.addshape("rocketship.gif")
tina = turtle.Turtle()
tina.shape("filename.png")

#sense.display_image('mario')

