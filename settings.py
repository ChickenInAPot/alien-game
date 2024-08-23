class Settings():

    def __init__(self):
        self.screenWidth = 1200
        self.screenHeight = 800
        self.bg = (100,100,100)

        self.shiplimit = 3
        

        self.bulletwidth = 3
        self.bulletheight =15
        self.bulletcolor = (255, 60, 60)
        
        self.bulletsallowed = 3

 
        self.fleetdropspeed = 10
        self.speedup = 1.1
        
        self.numstars = 50

        self.initalizedynamicsettings()

    def initalizedynamicsettings(self):
        self.alienspeed = 2
        self.bulletspeed = 15
        self.fleetdir = 1

    def increasespeed(self):
        self.bulletspeed *= self.speedup
        self.alienspeed *= self.speedup
