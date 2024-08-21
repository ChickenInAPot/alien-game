import pygame.font


class Button():

    def __init__(self, settings, screen, msg):

        self.screen = screen
        self.screenrect = self.screen.get_rect()


        self.width, self.height = 200, 50
        self.buttoncolor = (0,255,0)
        self.textcolor = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0 , 0, self.width, self.height)
        self.rect.center = self.screenrect.center

        self.prepmsg(msg)
    
    def prepmsg(self, msg):

        self.msgimg = self.font.render(msg, True, self.textcolor, self.buttoncolor)
        self.msgimgrect = self.msgimg.get_rect()
        self.msgimgrect.center = self.rect.center

    def drawbutton(self):
        self.screen.fill(self.buttoncolor, self.rect)
        self.screen.blit(self.msgimg, self.msgimgrect)
