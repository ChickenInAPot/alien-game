import pygame
from utils import scaleimg

class Ship():

    def __init__(self, settings, screen):
        self.screen = screen
        
        self.settings = settings

        self.image = scaleimg('imgs/spaceship.png', 0.1)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.movingr = False
        self.movingl = False

    def update(self):
        if self.movingr and self.rect.right < self.screen_rect.right:
            self.rect.centerx +=5
        if self.movingl and self.rect.left > 0:
            self.rect.centerx -=5
            
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx


