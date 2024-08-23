import pygame
from utils import scaleimg
from pygame.sprite import Sprite

class Star(Sprite):

    def __init__(self, screen,x , y):

        super().__init__()
        self.screen = screen

        self.img = scaleimg('imgs/star.png', 0.1)
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y


    def drawstars(self):
        self.screen.blit(self.img, self.rect)