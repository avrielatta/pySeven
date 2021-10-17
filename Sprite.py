import pygame, math

class Sprite(pygame.sprite.Sprite):

    def __init__(self, surf, color, width, height, point):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surf
        self.color = color
        self.width = width
        self.height = height
        self.point = point

        
    def draw(self):
        pygame.draw.polygon(self.surf, self.color, self.point)
        