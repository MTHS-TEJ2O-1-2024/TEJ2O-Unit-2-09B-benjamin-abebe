"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *
import random

# defining variables
random_number = 0
score = 0

scissor = Image("99009:"
                "99090:"
                "00900:"
                "99090:"
                "99009")

display.clear()
display.show(Image.HAPPY)

while True:
    if accelerometer.was_gesture("shake"):
        random_number = random.randint(0, 2)
        display.clear()

        # if random_number == 0
        if random_number == 0:
            display.show(Image.SQUARE_SMALL)
            sleep(3000)
            display.show(Image.HAPPY)

        # if random_number == 1
        if random_number == 1:
            display.show(Image.SQUARE)
            sleep(3000)
            display.show(Image.HAPPY)

        # if random_number == 2
        if random_number == 2:
            display.show(scissor)
            sleep(3000)  
            display.show(Image.HAPPY)

    
    # if button a is pressed
    if button_a.is_pressed():
        score += 1
        display.show(Image.YES)
        sleep(1000)  
        display.show(Image.HAPPY)

    # if button b is pressed
    if button_b.is_pressed():
        display.scroll("Score: " + str(score)) 
        sleep(1000)
        display.clear()
