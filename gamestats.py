class GameStats():

    def __init__(self, settings):

        self.settings = settings
        self.resetstats()
        self.gameactive = False
        

    def resetstats(self):
        self.shipsleft = self.settings.shiplimit
        self.score = 0

