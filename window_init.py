import pygame

def window_init(width, height, color):
    window = pygame.display.set_mode((width, height))
    window.fill(color)
    return window