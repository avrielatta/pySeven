# Imports
import pygame, sys
from window_init import window_init
from Sprite import Sprite
from calc_pos import calc_pos
from const import *



# Initialize pygame
pygame.init()

window = window_init(WINDOW_WIDTH, WINDOW_HEIGHT, BLACK)

def inc(n):
    return n + 0.1

def main():

    z = 0.5
    z1 = 0.5

    while 1:
        print(z)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        sprite = Sprite(window, WHITE, WINDOW_WIDTH, WINDOW_HEIGHT, [calc_pos(-50, -50, z), calc_pos(50, -50, 0.5), calc_pos(50, 50, z1), calc_pos(-50, 50, 0.5)])
        sprite.draw()
        pygame.display.update()
        window.fill(BLACK)
        z += 0.001
        z1 -= 0.001

if __name__ == '__main__': main()