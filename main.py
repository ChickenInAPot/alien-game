import pygame
from pygame.sprite import Group
from settings import Settings
from utils import  scaleimg
from ship import  Ship
import gamefuncs as gf
from alien import Alien
from gamestats import GameStats
from button import Button
from scoreboard import Scoreboard

def runGame():
    pygame.init()
    gameSettings = Settings()
    screen = pygame.display.set_mode((gameSettings.screenWidth, gameSettings.screenHeight))
    pygame.display.set_caption("Alien Invasion")

    
    playbutton = Button(gameSettings, screen, "PLAY")
     
    stats = GameStats(gameSettings)

    ship = Ship(gameSettings, screen)
    bullets = Group()
    aliens = Group()
    gf.createfleet(gameSettings, screen, ship, aliens) 
    sb = Scoreboard(gameSettings, screen, stats)

    while True:
        gf.checkevnt(gameSettings, screen, stats, playbutton, ship, aliens,bullets)
        if stats.gameactive:
            ship.update()
            gf.updatealiens(gameSettings, stats, screen, ship, aliens, bullets)
            gf.updatebullets(gameSettings, screen,stats, sb, ship, aliens, bullets)
        gf.updatescreen(gameSettings, screen, stats, sb, ship, aliens, bullets,playbutton)
            
if __name__ == "__main__":
    runGame()