import pygame
from pygame.sprite import Sprite
from utils import scaleimg

class Alien(Sprite):

    def __init__(self, settings, screen):

        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = scaleimg('imgs/alien.webp', 0.1)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):

        self.x += (self.settings.alienspeed * self.settings.fleetdir)
        self.rect.x = self.x

    def checkedges(self):

        screenrect  = self.screen.get_rect()
        if self.rect.right >= screenrect.right:
            return True
        elif self.rect.left <= 0:
            return True

 