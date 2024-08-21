import pygame.font

class Scoreboard():

    def __init__(self, settings, screen, stats):

        self.screen = screen
        self.screenrect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.textcolor = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)


        self.prepscore()

    def prepscore(self):

        scorestr = str(self.stats.score)
        self.scoreimg = self.font.render(scorestr, True, self.textcolor, self.settings.bg)
        self.scorerect = self.scoreimg.get_rect()
        self.scorerect.right = self.screenrect.right - 20
        self.scorerect.top = 20


    def showscore(self):
        self.screen.blit(self.scoreimg, self.scorerect)


