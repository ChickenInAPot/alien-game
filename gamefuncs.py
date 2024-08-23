import sys
import pygame
from bullet import Bullet
from alien import Alien
from stars import Star
from time import sleep
import random

def checkdown(event, settings, screen, ship, bullets):
    if event.key == pygame.K_d:
        ship.movingr = True
    elif event.key == pygame.K_a:
        ship.movingl = True 
    elif event.key == pygame.K_SPACE:
        firebullet(settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def checkup(event, ship):
    if event.key == pygame.K_d:
        ship.movingr = False
    elif event.key == pygame.K_a:
        ship.movingl = False

def checkevnt(settings, screen, stats, playbutton, ship, aliens,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkdown(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkup(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            checkplaybutton(settings, screen, stats, playbutton, ship, aliens,bullets, mouse_x, mouse_y)

def checkplaybutton(settings, screen, stats, playbutton, ship, aliens,bullets, mouse_x, mouse_y):
    buttonclicked = playbutton.rect.collidepoint(mouse_x,mouse_y)
    if buttonclicked and not stats.gameactive:
        settings.initalizedynamicsettings()
        pygame.mouse.set_visible(False)
        stats.resetstats()
        stats.gameactive = True

        aliens.empty()
        bullets.empty()

        createfleet(settings, screen, ship, aliens)
        ship.center_ship()

def updatescreen(settings, screen, stats, sb, ship, aliens, bullets,playbutton, stars):
    screen.fill(settings.bg)
    for star in stars.sprites():
        star.drawstars()
    for bullet in bullets.sprites():
        bullet.drawbullet()
    ship.blitme()
    aliens.draw(screen)
    sb.showscore()
    

    if not stats.gameactive:
        playbutton.drawbutton()

    
    pygame.display.flip()

def firebullet(settings, screen, ship, bullets):
    if len(bullets) < settings.bulletsallowed:
        newbullet = Bullet(settings, screen, ship)
        bullets.add(newbullet)

def updatebullets(settings, screen,stats, sb, ship, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        stats.score += 50
        sb.prepscore()

    if len(aliens) == 0:
        bullets.empty()
        createfleet(settings, screen, ship, aliens)
        settings.increasespeed()

def getnumrows(settings, shipheight, alienheight):
    availablespacey = settings.screenHeight - (3 * alienheight) - shipheight
    numrows = int(availablespacey / (2 * alienheight))
    return numrows  # Return the calculated number of rows

def getnumaliens(settings, alienwidth):
    availablespacex = settings.screenWidth - 2 * alienwidth
    numberaliensx = int(availablespacex / (2 * alienwidth))
    return numberaliensx

def createalien(settings, screen, aliens, aliennum, rownum):
    alien = Alien(settings, screen)
    alienwidth = alien.rect.width
    alien.x = alienwidth + 2 * alienwidth * aliennum
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * rownum
    aliens.add(alien)

def createfleet(settings, screen, ship, aliens):
    alien = Alien(settings, screen)
    alienwidth = alien.rect.width
    numberaliensx = getnumaliens(settings, alienwidth)
    numrows = getnumrows(settings, ship.rect.height, alien.rect.height)
    for rownum in range(numrows):
        for aliennum in range(numberaliensx):
            createalien(settings, screen, aliens, aliennum, rownum)

def changefleetdir(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleetdropspeed
    settings.fleetdir *= -1 

def checkfleetedges(settings, aliens):
    for alien in aliens.sprites():
        if alien.checkedges():
            changefleetdir(settings, aliens)
            break

def shiphit(settings, stats, screen, ship, aliens, bullets):
    if stats.shipsleft > 0:
        stats.shipsleft -= 1 
        aliens.empty()
        bullets.empty()
        createfleet(settings, screen, ship, aliens)
        ship.center_ship()
    else:
        pygame.mouse.set_visible(True)
        stats.gameactive = False


    sleep(0.5)
def checkaliensbottom(settings, stats, screen, ship, aliens, bullets):
    screenrect = screen.get_rect()
    
    for alien in aliens.sprites():
        if alien.rect.bottom >= screenrect.bottom:

            shiphit(settings,stats,screen,ship,aliens,bullets)
                   
def updatealiens(settings, stats, screen, ship,  aliens, bullets):
    checkfleetedges(settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship,aliens):
        print("bald")
        shiphit(settings, stats, screen, ship, aliens, bullets)
    
        checkaliensbottom(settings, stats, screen, ship, aliens, bullets)


def initstars(stars, screen, settings):
    stars.empty()
    for i in range(5):
        x = random.randint(0, settings.screenWidth)
        y = random.randint(0, settings.screenHeight)
        newstar = Star(screen, x, y)
        stars.add()