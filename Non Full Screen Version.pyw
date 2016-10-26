#    15-112: Principles of Programming and Computer Science
#    Final Project: Football Game
#    Name      : Julian Sam
#    AndrewID  : julians
#    File Created: 11/14/2015 9:12AM 

########### Sources ##############
#Soccer Ball from (Free to Use): 
#http://www.iconarchive.com/show/metro-raster-sport-icons-by-icons-land/Soccer-Ball-icon.html#

#All other images were designed by me
#Make sure Pygame is installed and that monospace font is installed.


#Thanks Prof. Saquib. 
#Thanks Rohith K. Pillai
##################################


######## Imports ##############
import pygame
import random
import sys
from pygame.locals import *
###############################

# For future reference, any variable beginning with O- indicates red team
# -It is replication of the variable wihtout O, but for red team.


# This class is the blue team class.
class player():
    plU = pygame.image.load("Images/blueU.png")
    plD = pygame.image.load("Images/blueD.png")
    plL = pygame.image.load("Images/blueL.png")
    plR = pygame.image.load("Images/blueR.png")
    plUR = pygame.image.load("Images/blueUR.png")
    plUL = pygame.image.load("Images/blueUL.png")
    plDL = pygame.image.load("Images/blueDL.png")
    plDR = pygame.image.load("Images/blueDR.png")
    ### Load Active player images below, inactive above
    plAU = pygame.image.load("Images/blueAU.png")
    plAD = pygame.image.load("Images/blueAD.png")
    plAL = pygame.image.load("Images/blueAL.png")
    plAR = pygame.image.load("Images/blueAR.png")
    plAUR = pygame.image.load("Images/blueAUR.png")
    plAUL = pygame.image.load("Images/blueAUL.png")
    plADL = pygame.image.load("Images/blueADL.png")
    plADR = pygame.image.load("Images/blueADR.png")

    yupperLimit = 64
    ylowerLimit = 780
    xupperLimit = 40
    xlowerLimit = 1115
    #Limits for the player not to go past the field boundaries


    def __init__(self,x,y,velocity, position, active = False, img = plR, imgA = plAR):
        self.x = x
        self.y = y
        self.velocity = velocity   
        self.active = active
        self.img = img
        self.imgA = imgA
        self.position = position
        self.counter = 0
        # initialize x, y positions, velocity of player, active means wheter the player is user controlled or not
        #img is nonUsercontrolled Image and imgA is usercontrolled Image
        #self.counter is used for AI timing, and making AI movements smooth


    def setxy(self,x,y, active, img = plL, imgA = plAL):
        self.x = x
        self.y = y
        self.img = img
        self.imgA = imgA
    # Set function for x and y of the player

    def Activate(self):
        self.active = True
    def deActivate(self):
        self.active = False
    #change active state for the player

    #draw the image onto the screen
    def draw(self):
        if self.active == True:
            screen.blit(self.imgA, [self.x, self.y])
        else:
            screen.blit(self.img, [self.x, self.y])



    # Main AI function for all the players
    # AI is player position based
    # Due to length and repitition of the AI function, all explanation of AI will go here:
    # self.active makes sure the player isnt user controlled when AI moved
    # self.counter % 2 slows down the player and makes it go at a reasonable speed for AI

    # AI for GoalKeeper:
    #     If out of position, go to position


    # AI for Defensive Player:
    #     Imagine a rectangular box for which each defensive player resides,
    #         If the player leaves the rectangle, go back to it.
    #         If the player is in the rectangle and the opponent has the ball, go tackle the player
    #         If the player is in the rectangle and the ball is outside, move relative to the x-position of the ball

    # AI for MidField Players:
    #     Imagine a rectangular box for which each midfield player resides,
    #         If the player leaves the rectangle, go back to it.
    #         If the player is in the rectangle and the opponent has the ball, go tackle the player
    #         If the player is in the rectangle and the ball is outside, move relative to the x-position of the ball

    # AI for Attacking Players:
    #     Imagine a rectangular box for which each defensive player resides,
    #         If the player leaves the rectangle, go back to it.
    #         If the player is in the rectangle and the opponent has the ball, go tackle the player
    #         If the player is in the rectangle and the ball is outside, move relative to the x-position of the ball
    #         If ball is ahead, get ahead and ready to attack



    def TeamMateMovement(self,ball):
      
        if self.position == "gk":
            if self.active == False:

                if self.counter % 2 == 0:
            
                    self.defaultPositionx = 60
                    self.defaultPositiony = 414
                    if self.x > self.defaultPositionx and self.y > self.defaultPositiony:
                        self.x -= 1
                        self.y -= 1
                        self.img = player.plUL
                        self.imgA = player.plAUL

                    elif self.x > self.defaultPositionx and self.y < self.defaultPositiony:
                        self.x -= 1
                        self.y += 1
                        self.img = player.plDL
                        self.imgA = player.plADL

                    elif self.x < self.defaultPositionx and self.y > self.defaultPositiony:
                        self.x += 1
                        self.y -= 1
                        self.img = player.plUR
                        self.imgA = player.plAUR

                    elif self.x < self.defaultPositionx and self.y < self.defaultPositiony:
                        self.x += 1
                        self.y += 1
                        self.img = player.plDR
                        self.imgA = player.plADR


                    elif self.x > self.defaultPositionx:
                        self.x -= 1
                        self.img = player.plL
                        self.imgA = player.plAL
                    elif self.x < self.defaultPositionx:
                        self.x += 1
                        self.img = player.plR
                        self.imgA = player.plAR
                    elif self.y > self.defaultPositiony:
                        self.y -= 1
                        self.img = player.plU
                        self.imgA = player.plAU
                    elif self.y < self.defaultPositiony:
                        self.y += 1
                        self.img = player.plD
                        self.imgA = player.plAD

                    if self.x == self.defaultPositionx and self.y == self.defaultPositiony:
                        self.img = player.plR
                        self.imgA = player.plAR
                        self.counter = 0

            self.counter+= 1


        if self.position == "midUp":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1150 or self.x < 241 or self.y > 200 or self.y < 100:
                        if self.x > 1150 and self.y > 200:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = player.plUL
                            self.imgA = player.plAUL

                        elif self.x > 1150 and self.y < 100:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = player.plDL
                            self.imgA = player.plADL
                        elif self.x < 241 and self.y > 200:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = player.plUR
                            self.imgA = player.plAUR

                        elif self.x < 241 and self.y < 100:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = player.plDR
                            self.imgA = player.plADR

                        elif self.x > 1150:
                            self.x = self.x - 2
                            self.img = player.plL
                            self.imgA = player.plAL
                        elif self.x < 241:
                            self.x = self.x + 2
                            self.img = player.plR
                            self.imgA = player.plAR 
                        elif self.y > 200:
                            self.y = self.y - 2
                            self.img = player.plU
                            self.imgA = player.plAU
                        elif self.y < 100:
                            self.y = self.y + 2
                            self.img = player.plD
                            self.imgA = player.plAD

        
                    else:
                        if (ball.x < 242):
                            self.defaultPositionx = 242
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 

                        elif (ball.x > 951 or ball.x < 241) or (ball.y > 300 or ball.y < 67):
                            self.defaultPositionx = ball.x - 100
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plR
                                self.imgA = player.plAR
                            
                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 
                        else:
                            if ball.getStuck() == False:
                                if self.x > ball.x and self.y > ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = player.plUL
                                    self.imgA = player.plAUL

                                elif self.x > ball.x and self.y < ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = player.plDL
                                    self.imgA = player.plADL

                                elif self.x < ball.x and self.y > ball.y + 25:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = player.plUR
                                    self.imgA = player.plAUR

                                elif self.x < ball.x and self.y < ball.y + 25:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = player.plDR
                                    self.imgA = player.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                                elif self.y > ball.y + 25:
                                    self.y = self.y - 2
                                    self.img = player.plU
                                    self.imgA = player.plAU
                                elif self.y < ball.y + 25:
                                    self.y = self.y + 2
                                    self.img = player.plD
                                    self.imgA = player.plAD

        

            self.counter += 1
    

        if self.position == "midDown": 
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1150 or self.x < 241 or self.y > 800 or self.y < 650:
                        if self.x > 1150 and self.y > 800:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = player.plUL
                            self.imgA = player.plAUL

                        elif self.x > 1150 and self.y < 650:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = player.plDL
                            self.imgA = player.plADL
                        elif self.x < 241 and self.y > 800:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = player.plUR
                            self.imgA = player.plAUR

                        elif self.x < 241 and self.y < 650:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = player.plDR
                            self.imgA = player.plADR

                        elif self.x > 1150:
                            self.x = self.x - 2
                            self.img = player.plL
                            self.imgA = player.plAL
                        elif self.x < 241:
                            self.x = self.x + 2
                            self.img = player.plR
                            self.imgA = player.plAR 
                        elif self.y > 800:
                            self.y = self.y - 2
                            self.img = player.plU
                            self.imgA = player.plAU
                        elif self.y < 650:
                            self.y = self.y + 2
                            self.img = player.plD
                            self.imgA = player.plAD

        
                    else:
                        if (ball.x < 242):
                            self.defaultPositionx = 242
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 

                        elif (ball.x > 951 or ball.x < 241) or (ball.y > 810 or ball.y < 600):
                            self.defaultPositionx = ball.x - 100
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plR
                                self.imgA = player.plAR
                            
                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 
                        else:
                            if ball.getStuck() == False:
                                if self.x > ball.x and self.y > ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = player.plUL
                                    self.imgA = player.plAUL

                                elif self.x > ball.x and self.y < ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = player.plDL
                                    self.imgA = player.plADL

                                elif self.x < ball.x and self.y > ball.y + 25:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = player.plUR
                                    self.imgA = player.plAUR

                                elif self.x < ball.x and self.y < ball.y + 25:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = player.plDR
                                    self.imgA = player.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                                elif self.y > ball.y + 25:
                                    self.y = self.y - 2
                                    self.img = player.plU
                                    self.imgA = player.plAU
                                elif self.y < ball.y + 25:
                                    self.y = self.y + 2
                                    self.img = player.plD
                                    self.imgA = player.plAD
                   
            self.counter += 1

        if self.position == "att":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1050 or self.x < 380 or self.y > 600 or self.y < 300:
                        if self.x > 1150 and self.y > 600:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = player.plUL
                            self.imgA = player.plAUL

                        elif self.x > 1050 and self.y < 300:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = player.plDL
                            self.imgA = player.plADL
                        elif self.x < 380 and self.y > 600:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = player.plUR
                            self.imgA = player.plAUR

                        elif self.x < 380 and self.y < 300:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = player.plDR
                            self.imgA = player.plADR

                        elif self.x > 1050:
                            self.x = self.x - 2
                            self.img = player.plL
                            self.imgA = player.plAL
                        elif self.x < 380:
                            self.x = self.x + 2
                            self.img = player.plR
                            self.imgA = player.plAR 
                        elif self.y > 600:
                            self.y = self.y - 2
                            self.img = player.plU
                            self.imgA = player.plAU
                        elif self.y < 300:
                            self.y = self.y + 2
                            self.img = player.plD
                            self.imgA = player.plAD

                    
                    else:

                        if (ball.x < 380):
                            self.defaultPositionx = 380
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 

                        else:
                            if ball.getStuck() == True: #ball.x > 1050 or ball.x < 380) or (ball.y > 300 or ball.y < 600
                                self.defaultPositionx = ball.x - 50
                                if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                    self.img = player.plR
                                    self.imgA = player.plAR
                                
                                elif self.x > self.defaultPositionx:
                                    self.x -= 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < self.defaultPositionx:
                                    self.x += 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                            elif ball.getStuck() == False:
                                if self.x > ball.x and self.y > ball.y :
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = player.plUL
                                    self.imgA = player.plAUL

                                elif self.x > ball.x and self.y < ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = player.plDL
                                    self.imgA = player.plADL

                                elif self.x < ball.x and self.y > ball.y:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = player.plUR
                                    self.imgA = player.plAUR

                                elif self.x < ball.x and self.y < ball.y:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = player.plDR
                                    self.imgA = player.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                                elif self.y > ball.y :
                                    self.y = self.y - 2
                                    self.img = player.plU
                                    self.imgA = player.plAU
                                elif self.y < ball.y :
                                    self.y = self.y + 2
                                    self.img = player.plD
                                    self.imgA = player.plAD
            self.counter += 1



        if self.position == "def":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 451 or self.x < 250 or self.y > 600 or self.y < 220:
                        if self.x > 451 and self.y > 600:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = player.plUL
                            self.imgA = player.plAUL

                        elif self.x > 451 and self.y < 220:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = player.plDL
                            self.imgA = player.plADL
                        elif self.x < 250 and self.y > 600:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = player.plUR
                            self.imgA = player.plAUR

                        elif self.x < 250 and self.y < 220:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = player.plDR
                            self.imgA = player.plADR

                        elif self.x > 451:
                            self.x = self.x - 2
                            self.img = player.plL
                            self.imgA = player.plAL
                        elif self.x < 250:
                            self.x = self.x + 2
                            self.img = player.plR
                            self.imgA = player.plAR 
                        elif self.y > 600:
                            self.y = self.y - 2
                            self.img = player.plU
                            self.imgA = player.plAU
                        elif self.y < 220:
                            self.y = self.y + 2
                            self.img = player.plD
                            self.imgA = player.plAD

                    
                    else:
                        if (ball.x >=451):
                            self.defaultPositionx = 451
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plR
                                self.imgA = player.plAR

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 

                        else:
                            if ball.getStuck() == True:
                                self.defaultPositionx = ball.x - 100
                                if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                    self.img = player.plR
                                    self.imgA = player.plAR

                                elif self.x > self.defaultPositionx:
                                    self.x -= 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < self.defaultPositionx:
                                    self.x += 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                            elif ball.getStuck() == False:
                                if self.x > ball.x and self.y > ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = player.plUL
                                    self.imgA = player.plAUL

                                elif self.x > ball.x and self.y < ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = player.plDL
                                    self.imgA = player.plADL

                                elif self.x < ball.x and self.y > ball.y:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = player.plUR
                                    self.imgA = player.plAUR

                                elif self.x < ball.x and self.y < ball.y:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = player.plDR
                                    self.imgA = player.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                                elif self.y > ball.y :
                                    self.y = self.y - 2
                                    self.img = player.plU
                                    self.imgA = player.plAU
                                elif self.y < ball.y :
                                    self.y = self.y + 2
                                    self.img = player.plD
                                    self.imgA = player.plAD
            self.counter += 1




    # Since halftime changes the position of the players, this function applies the Same AI above, 
    # but for the switched postions.

    def HalfTimeTeamMateMovement(self,ball):
        if self.position == "gk":
            if self.active == False:

                if self.counter % 2 == 0:
            
                    self.defaultPositionx = 1090
                    self.defaultPositiony = 414
                    if self.x > self.defaultPositionx and self.y > self.defaultPositiony:
                        self.x -= 1
                        self.y -= 1
                        self.img = player.plUL
                        self.imgA = player.plAUL

                    elif self.x > self.defaultPositionx and self.y < self.defaultPositiony:
                        self.x -= 1
                        self.y += 1
                        self.img = player.plDL
                        self.imgA = player.plADL

                    elif self.x < self.defaultPositionx and self.y > self.defaultPositiony:
                        self.x += 1
                        self.y -= 1
                        self.img = player.plUR
                        self.imgA = player.plAUR

                    elif self.x < self.defaultPositionx and self.y < self.defaultPositiony:
                        self.x += 1
                        self.y += 1
                        self.img = player.plDR
                        self.imgA = player.plADR


                    elif self.x > self.defaultPositionx:
                        self.x -= 1
                        self.img = player.plL
                        self.imgA = player.plAL
                    elif self.x < self.defaultPositionx:
                        self.x += 1
                        self.img = player.plR
                        self.imgA = player.plAR
                    elif self.y > self.defaultPositiony:
                        self.y -= 1
                        self.img = player.plU
                        self.imgA = player.plAU
                    elif self.y < self.defaultPositiony:
                        self.y += 1
                        self.img = player.plD
                        self.imgA = player.plAD

                    if self.x == self.defaultPositionx and self.y == self.defaultPositiony:
                        self.img = player.plL
                        self.imgA = player.plAL
                        self.counter = 0

            self.counter+= 1



        if self.position == "midUp":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1000 or self.x < 150 or self.y > 200 or self.y < 100:

                        if self.x > 1000 and self.y > 200:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = player.plUL
                            self.imgA = player.plAUL

                        elif self.x > 1000 and self.y < 100:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = player.plDL
                            self.imgA = player.plADL
                        elif self.x < 150 and self.y > 200:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = player.plUR
                            self.imgA = player.plAUR

                        elif self.x < 150 and self.y < 100:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = player.plDR
                            self.imgA = player.plADR

                        elif self.x > 1000:
                            self.x = self.x - 2
                            self.img = player.plL
                            self.imgA = player.plAL
                        elif self.x < 150:
                            self.x = self.x + 2
                            self.img = player.plR
                            self.imgA = player.plAR 
                        elif self.y > 200:
                            self.y = self.y - 2
                            self.img = player.plU
                            self.imgA = player.plAU
                        elif self.y < 100:
                            self.y = self.y + 2
                            self.img = player.plD
                            self.imgA = player.plAD

        
                    else:
                        if (ball.x > 1000):
                            self.defaultPositionx = 1000
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plR
                                self.imgA = player.plAR

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 


                        elif (ball.x > 951 or ball.x < 241) or (ball.y > 300 or ball.y < 67):
                            self.defaultPositionx = ball.x + 100
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plL
                                self.imgA = player.plAL
                            
                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 
                        else:
                            if ball.getStuck() == False:
                                if self.x > ball.x and self.y > ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = player.plUL
                                    self.imgA = player.plAUL

                                elif self.x > ball.x and self.y < ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = player.plDL
                                    self.imgA = player.plADL

                                elif self.x < ball.x and self.y > ball.y + 25:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = player.plUR
                                    self.imgA = player.plAUR

                                elif self.x < ball.x and self.y < ball.y + 25:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = player.plDR
                                    self.imgA = player.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                                elif self.y > ball.y + 25:
                                    self.y = self.y - 2
                                    self.img = player.plU
                                    self.imgA = player.plAU
                                elif self.y < ball.y + 25:
                                    self.y = self.y + 2
                                    self.img = player.plD
                                    self.imgA = player.plAD
            self.counter += 1

        if self.position == "midDown": 
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1000 or self.x < 150 or self.y > 800 or self.y < 650:
                        if self.x > 1000 and self.y > 800:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = player.plUL
                            self.imgA = player.plAUL

                        elif self.x > 1000 and self.y < 650:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = player.plDL
                            self.imgA = player.plADL
                        elif self.x < 150 and self.y > 800:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = player.plUR
                            self.imgA = player.plAUR

                        elif self.x < 150 and self.y < 650:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = player.plDR
                            self.imgA = player.plADR

                        elif self.x > 1000:
                            self.x = self.x - 2
                            self.img = player.plL
                            self.imgA = player.plAL
                        elif self.x < 150:
                            self.x = self.x + 2
                            self.img = player.plR
                            self.imgA = player.plAR 
                        elif self.y > 800:
                            self.y = self.y - 2
                            self.img = player.plU
                            self.imgA = player.plAU
                        elif self.y < 650:
                            self.y = self.y + 2
                            self.img = player.plD
                            self.imgA = player.plAD

        
                    else:
                        if (ball.x < 242):
                            self.defaultPositionx = 242
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 

                        elif (ball.x > 951 or ball.x < 241) or (ball.y > 810 or ball.y < 600):
                            self.defaultPositionx = ball.x + 100
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plR
                                self.imgA = player.plAR
                            
                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 
                        else:
                            if ball.getStuck() == False:
                                if self.x > ball.x and self.y > ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = player.plUL
                                    self.imgA = player.plAUL

                                elif self.x > ball.x and self.y < ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = player.plDL
                                    self.imgA = player.plADL

                                elif self.x < ball.x and self.y > ball.y + 25:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = player.plUR
                                    self.imgA = player.plAUR

                                elif self.x < ball.x and self.y < ball.y + 25:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = player.plDR
                                    self.imgA = player.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                                elif self.y > ball.y + 25:
                                    self.y = self.y - 2
                                    self.img = player.plU
                                    self.imgA = player.plAU
                                elif self.y < ball.y + 25:
                                    self.y = self.y + 2
                                    self.img = player.plD
                                    self.imgA = player.plAD
                   
            self.counter += 1




        if self.position == "att":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 850 or self.x < 125 or self.y > 600 or self.y < 300:
                        if self.x > 1150 and self.y > 600:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = player.plUL
                            self.imgA = player.plAUL

                        elif self.x > 850 and self.y < 300:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = player.plDL
                            self.imgA = player.plADL
                        elif self.x < 125 and self.y > 600:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = player.plUR
                            self.imgA = player.plAUR

                        elif self.x < 125 and self.y < 300:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = player.plDR
                            self.imgA = player.plADR

                        elif self.x > 850:
                            self.x = self.x - 2
                            self.img = player.plL
                            self.imgA = player.plAL
                        elif self.x < 125:
                            self.x = self.x + 2
                            self.img = player.plR
                            self.imgA = player.plAR 
                        elif self.y > 600:
                            self.y = self.y - 2
                            self.img = player.plU
                            self.imgA = player.plAU
                        elif self.y < 300:
                            self.y = self.y + 2
                            self.img = player.plD
                            self.imgA = player.plAD

                    
                    else:

                        if (ball.x > 850):
                            self.defaultPositionx = 850
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plR
                                self.imgA = player.plAR

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 

                        else:
                            if ball.getStuck() == True: #ball.x > 1050 or ball.x < 380) or (ball.y > 300 or ball.y < 600
                                self.defaultPositionx = ball.x + 50

                                if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                    self.img = player.plR
                                    self.imgA = player.plAR
                                
                                elif self.x > self.defaultPositionx:
                                    self.x -= 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < self.defaultPositionx:
                                    self.x += 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                            elif ball.getStuck() == False:
                                if self.x > ball.x and self.y > ball.y :
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = player.plUL
                                    self.imgA = player.plAUL

                                elif self.x > ball.x and self.y < ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = player.plDL
                                    self.imgA = player.plADL

                                elif self.x < ball.x and self.y > ball.y:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = player.plUR
                                    self.imgA = player.plAUR

                                elif self.x < ball.x and self.y < ball.y:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = player.plDR
                                    self.imgA = player.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                                elif self.y > ball.y :
                                    self.y = self.y - 2
                                    self.img = player.plU
                                    self.imgA = player.plAU
                                elif self.y < ball.y :
                                    self.y = self.y + 2
                                    self.img = player.plD
                                    self.imgA = player.plAD
            self.counter += 1

        if self.position == "def":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 953 or self.x < 653 or self.y > 600 or self.y < 220:
                        if self.x > 953 and self.y > 600:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = player.plUL
                            self.imgA = player.plAUL

                        elif self.x > 953 and self.y < 220:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = player.plDL
                            self.imgA = player.plADL
                        elif self.x < 653 and self.y > 600:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = player.plUR
                            self.imgA = player.plAUR

                        elif self.x < 653 and self.y < 220:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = player.plDR
                            self.imgA = player.plADR

                        elif self.x > 953:
                            self.x = self.x - 2
                            self.img = player.plL
                            self.imgA = player.plAL
                        elif self.x < 653:
                            self.x = self.x + 2
                            self.img = player.plR
                            self.imgA = player.plAR 
                        elif self.y > 600:
                            self.y = self.y - 2
                            self.img = player.plU
                            self.imgA = player.plAU
                        elif self.y < 220:
                            self.y = self.y + 2
                            self.img = player.plD
                            self.imgA = player.plAD

                    
                    else:
                        if (ball.x < 653):
                            self.defaultPositionx = 653
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = player.plL
                                self.imgA = player.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = player.plR
                                self.imgA = player.plAR 

                        else:
                            if ball.getStuck() == True:
                                self.defaultPositionx = ball.x + 100
                                if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                    self.img = player.plR
                                    self.imgA = player.plAR

                                elif self.x > self.defaultPositionx:
                                    self.x -= 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < self.defaultPositionx:
                                    self.x += 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                            elif ball.getStuck() == False:
                                if self.x > ball.x and self.y > ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = player.plUL
                                    self.imgA = player.plAUL

                                elif self.x > ball.x and self.y < ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = player.plDL
                                    self.imgA = player.plADL

                                elif self.x < ball.x and self.y > ball.y:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = player.plUR
                                    self.imgA = player.plAUR

                                elif self.x < ball.x and self.y < ball.y:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = player.plDR
                                    self.imgA = player.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = player.plL
                                    self.imgA = player.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = player.plR
                                    self.imgA = player.plAR 

                                elif self.y > ball.y :
                                    self.y = self.y - 2
                                    self.img = player.plU
                                    self.imgA = player.plAU
                                elif self.y < ball.y :
                                    self.y = self.y + 2
                                    self.img = player.plD
                                    self.imgA = player.plAD
            self.counter += 1



    # Function used to move the player from user controls.
    # The y and x lower and upper limits are the boundaries of the field.

    # The variable direction which is passed in is which way the user wishes the player to go
    
    # The function also has img and imgA from each direction, which updates the picture based 
    # on the direction the player is going


    def Move(self,direction):  
        if direction == 'UP' and self.y > self.yupperLimit:
            self.y -= self.velocity
            self.img = self.plU
            self.imgA = self.plAU
                
        elif direction == 'DOWN' and self.y <= self.ylowerLimit:
            self.y += self.velocity           
            self.img = self.plD
            self.imgA = self.plAD
                    
        elif direction == 'LEFT' and self.x > self.xupperLimit:
            self.x -= self.velocity
            self.img = self.plL
            self.imgA = self.plAL

        elif direction == 'RIGHT' and self.x <= self.xlowerLimit:
            self.x += self.velocity
            self.img = self.plR
            self.imgA = self.plAR

        elif direction == 'UPLEFT' and self.y > self.yupperLimit and self.x > self.xupperLimit:
            self.y -= self.velocity
            self.x -= self.velocity
            self.img = self.plUL
            self.imgA = self.plAUL

        elif direction == 'UPRIGHT' and self.y > self.yupperLimit and self.x <= self.xlowerLimit:
            self.y -= self.velocity
            self.x += self.velocity
            self.img = self.plUR
            self.imgA = self.plAUR

        elif direction == 'DOWNLEFT' and self.y <= self.ylowerLimit and self.x > self.xupperLimit:
            self.y += self.velocity
            self.x -= self.velocity
            self.img = self.plDL
            self.imgA = self.plADL

        elif direction == 'DOWNRIGHT' and self.y <= self.ylowerLimit and self.x <= self.xlowerLimit:
            self.y += self.velocity
            self.x += self.velocity
            self.img = self.plDR
            self.imgA = self.plADR

##################################################################################################################################################


# THe red team class. Symmetric and Mirroring the Blue team player class
class OPlayer():
    plU = pygame.image.load("Images/redU.png")
    plD = pygame.image.load("Images/redD.png")
    plL = pygame.image.load("Images/redL.png")
    plR = pygame.image.load("Images/redR.png")
    plUR = pygame.image.load("Images/redUR.png")
    plUL = pygame.image.load("Images/redUL.png")
    plDL = pygame.image.load("Images/redDL.png")
    plDR = pygame.image.load("Images/redDR.png")
    ### Load Active player images below, inactive above
    plAU = pygame.image.load("Images/redAU.png")
    plAD = pygame.image.load("Images/redAD.png")
    plAL = pygame.image.load("Images/redAL.png")
    plAR = pygame.image.load("Images/redAR.png")
    plAUR = pygame.image.load("Images/redAUR.png")
    plAUL = pygame.image.load("Images/redAUL.png")
    plADL = pygame.image.load("Images/redADL.png")
    plADR = pygame.image.load("Images/redADR.png")


    yupperLimit = 64
    ylowerLimit = 780
    xupperLimit = 40
    xlowerLimit = 1115

    #Limits for the player not to go past the field boundaries


    def __init__(self,x,y,velocity, position, active = False, img = plL, imgA = plAL):
        self.x = x
        self.y = y
        self.velocity = velocity   
        self.active = active
        self.img = img
        self.imgA = imgA
        self.position = position
        self.counter = 0
        # initialize x, y positions, velocity of player, active means wheter the player is user controlled or not
        #img is nonUsercontrolled Image and imgA is usercontrolled Image
        #self.counter is used for AI timing, and making AI movements smooth

    def setxy(self,x,y, active, img = plR, imgA = plAR):
        self.x = x
        self.y = y
        self.img = img
        self.imgA = imgA
   
    # Set function for x and y of the player


    def Activate(self):
        self.active = True
    def deActivate(self):
        self.active = False
    #change active state for the player

    #draw the image onto the screen

    def draw(self):
        if self.active == True:
            screen.blit(self.imgA, [self.x, self.y])
        else:
            screen.blit(self.img, [self.x, self.y])

    # Main AI function for all the players
    # AI is player position based
    # Due to length and repitition of the AI function, all explanation of AI will go here:
    # self.active makes sure the player isnt user controlled when AI moved
    # self.counter % 2 slows down the player and makes it go at a reasonable speed for AI

    # AI for GoalKeeper:
    #     If out of position, go to position


    # AI for Defensive Player:
    #     Imagine a rectangular box for which each defensive player resides,
    #         If the player leaves the rectangle, go back to it.
    #         If the player is in the rectangle and the opponent has the ball, go tackle the player
    #         If the player is in the rectangle and the ball is outside, move relative to the x-position of the ball

    # AI for MidField Players:
    #     Imagine a rectangular box for which each midfield player resides,
    #         If the player leaves the rectangle, go back to it.
    #         If the player is in the rectangle and the opponent has the ball, go tackle the player
    #         If the player is in the rectangle and the ball is outside, move relative to the x-position of the ball

    # AI for Attacking Players:
    #     Imagine a rectangular box for which each defensive player resides,
    #         If the player leaves the rectangle, go back to it.
    #         If the player is in the rectangle and the opponent has the ball, go tackle the player
    #         If the player is in the rectangle and the ball is outside, move relative to the x-position of the ball
    #         If ball is ahead, get ahead and ready to attack

    def TeamMateMovement(self,ball):
        if self.position == "gk":
            if self.active == False:

                if self.counter % 2 == 0:
            
                    self.defaultPositionx = 1090
                    self.defaultPositiony = 414
                    if self.x > self.defaultPositionx and self.y > self.defaultPositiony:
                        self.x -= 1
                        self.y -= 1
                        self.img = OPlayer.plUL
                        self.imgA = OPlayer.plAUL

                    elif self.x > self.defaultPositionx and self.y < self.defaultPositiony:
                        self.x -= 1
                        self.y += 1
                        self.img = OPlayer.plDL
                        self.imgA = OPlayer.plADL

                    elif self.x < self.defaultPositionx and self.y > self.defaultPositiony:
                        self.x += 1
                        self.y -= 1
                        self.img = OPlayer.plUR
                        self.imgA = OPlayer.plAUR

                    elif self.x < self.defaultPositionx and self.y < self.defaultPositiony:
                        self.x += 1
                        self.y += 1
                        self.img = OPlayer.plDR
                        self.imgA = OPlayer.plADR


                    elif self.x > self.defaultPositionx:
                        self.x -= 1
                        self.img = OPlayer.plL
                        self.imgA = OPlayer.plAL
                    elif self.x < self.defaultPositionx:
                        self.x += 1
                        self.img = OPlayer.plR
                        self.imgA = OPlayer.plAR
                    elif self.y > self.defaultPositiony:
                        self.y -= 1
                        self.img = OPlayer.plU
                        self.imgA = OPlayer.plAU
                    elif self.y < self.defaultPositiony:
                        self.y += 1
                        self.img = OPlayer.plD
                        self.imgA = OPlayer.plAD

                    if self.x == self.defaultPositionx and self.y == self.defaultPositiony:
                        self.img = OPlayer.plL
                        self.imgA = OPlayer.plAL
                        self.counter = 0

            self.counter+= 1



        if self.position == "midUp":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1000 or self.x < 150 or self.y > 200 or self.y < 100:

                        if self.x > 1000 and self.y > 200:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUL
                            self.imgA = OPlayer.plAUL

                        elif self.x > 1000 and self.y < 100:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = OPlayer.plDL
                            self.imgA = OPlayer.plADL
                        elif self.x < 150 and self.y > 200:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUR
                            self.imgA = OPlayer.plAUR

                        elif self.x < 150 and self.y < 100:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = OPlayer.plDR
                            self.imgA = OPlayer.plADR

                        elif self.x > 1000:
                            self.x = self.x - 2
                            self.img = OPlayer.plL
                            self.imgA = OPlayer.plAL
                        elif self.x < 150:
                            self.x = self.x + 2
                            self.img = OPlayer.plR
                            self.imgA = OPlayer.plAR 
                        elif self.y > 200:
                            self.y = self.y - 2
                            self.img = OPlayer.plU
                            self.imgA = OPlayer.plAU
                        elif self.y < 100:
                            self.y = self.y + 2
                            self.img = OPlayer.plD
                            self.imgA = OPlayer.plAD

        
                    else:
                        if (ball.x > 1000):
                            self.defaultPositionx = 1000
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 


                        elif (ball.x > 951 or ball.x < 241) or (ball.y > 300 or ball.y < 67):
                            self.defaultPositionx = ball.x + 100
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL
                            
                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 
                        else:
                            if ball.OgetStuck() == False:
                                if self.x > ball.x and self.y > ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUL
                                    self.imgA = OPlayer.plAUL

                                elif self.x > ball.x and self.y < ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDL
                                    self.imgA = OPlayer.plADL

                                elif self.x < ball.x and self.y > ball.y + 25:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUR
                                    self.imgA = OPlayer.plAUR

                                elif self.x < ball.x and self.y < ball.y + 25:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDR
                                    self.imgA = OPlayer.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                                elif self.y > ball.y + 25:
                                    self.y = self.y - 2
                                    self.img = OPlayer.plU
                                    self.imgA = OPlayer.plAU
                                elif self.y < ball.y + 25:
                                    self.y = self.y + 2
                                    self.img = OPlayer.plD
                                    self.imgA = OPlayer.plAD
            self.counter += 1


        if self.position == "midDown": 
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1000 or self.x < 150 or self.y > 800 or self.y < 650:
                        if self.x > 1000 and self.y > 800:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUL
                            self.imgA = OPlayer.plAUL

                        elif self.x > 1000 and self.y < 650:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = OPlayer.plDL
                            self.imgA = OPlayer.plADL
                        elif self.x < 150 and self.y > 800:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUR
                            self.imgA = OPlayer.plAUR

                        elif self.x < 150 and self.y < 650:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = OPlayer.plDR
                            self.imgA = OPlayer.plADR

                        elif self.x > 1000:
                            self.x = self.x - 2
                            self.img = OPlayer.plL
                            self.imgA = OPlayer.plAL
                        elif self.x < 150:
                            self.x = self.x + 2
                            self.img = OPlayer.plR
                            self.imgA = OPlayer.plAR 
                        elif self.y > 800:
                            self.y = self.y - 2
                            self.img = OPlayer.plU
                            self.imgA = OPlayer.plAU
                        elif self.y < 650:
                            self.y = self.y + 2
                            self.img = OPlayer.plD
                            self.imgA = OPlayer.plAD

        
                    else:
                        if (ball.x < 242):
                            self.defaultPositionx = 242
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 

                        elif (ball.x > 951 or ball.x < 241) or (ball.y > 810 or ball.y < 600):
                            self.defaultPositionx = ball.x + 100
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR
                            
                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 
                        else:
                            if ball.OgetStuck() == False:
                                if self.x > ball.x and self.y > ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUL
                                    self.imgA = OPlayer.plAUL

                                elif self.x > ball.x and self.y < ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDL
                                    self.imgA = OPlayer.plADL

                                elif self.x < ball.x and self.y > ball.y + 25:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUR
                                    self.imgA = OPlayer.plAUR

                                elif self.x < ball.x and self.y < ball.y + 25:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDR
                                    self.imgA = OPlayer.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                                elif self.y > ball.y + 25:
                                    self.y = self.y - 2
                                    self.img = OPlayer.plU
                                    self.imgA = OPlayer.plAU
                                elif self.y < ball.y + 25:
                                    self.y = self.y + 2
                                    self.img = OPlayer.plD
                                    self.imgA = OPlayer.plAD
                   
            self.counter += 1




        if self.position == "att":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 850 or self.x < 125 or self.y > 600 or self.y < 300:
                        if self.x > 1150 and self.y > 600:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUL
                            self.imgA = OPlayer.plAUL

                        elif self.x > 850 and self.y < 300:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = OPlayer.plDL
                            self.imgA = OPlayer.plADL
                        elif self.x < 125 and self.y > 600:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUR
                            self.imgA = OPlayer.plAUR

                        elif self.x < 125 and self.y < 300:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = OPlayer.plDR
                            self.imgA = OPlayer.plADR

                        elif self.x > 850:
                            self.x = self.x - 2
                            self.img = OPlayer.plL
                            self.imgA = OPlayer.plAL
                        elif self.x < 125:
                            self.x = self.x + 2
                            self.img = OPlayer.plR
                            self.imgA = OPlayer.plAR 
                        elif self.y > 600:
                            self.y = self.y - 2
                            self.img = OPlayer.plU
                            self.imgA = OPlayer.plAU
                        elif self.y < 300:
                            self.y = self.y + 2
                            self.img = OPlayer.plD
                            self.imgA = OPlayer.plAD

                    
                    else:

                        if (ball.x > 850):
                            self.defaultPositionx = 850
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 

                        else:
                            if ball.OgetStuck() == True: #ball.x > 1050 or ball.x < 380) or (ball.y > 300 or ball.y < 600
                                self.defaultPositionx = ball.x + 50

                                if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR
                                
                                elif self.x > self.defaultPositionx:
                                    self.x -= 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < self.defaultPositionx:
                                    self.x += 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                            elif ball.OgetStuck() == False:
                                if self.x > ball.x and self.y > ball.y :
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUL
                                    self.imgA = OPlayer.plAUL

                                elif self.x > ball.x and self.y < ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDL
                                    self.imgA = OPlayer.plADL

                                elif self.x < ball.x and self.y > ball.y:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUR
                                    self.imgA = OPlayer.plAUR

                                elif self.x < ball.x and self.y < ball.y:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDR
                                    self.imgA = OPlayer.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                                elif self.y > ball.y :
                                    self.y = self.y - 2
                                    self.img = OPlayer.plU
                                    self.imgA = OPlayer.plAU
                                elif self.y < ball.y :
                                    self.y = self.y + 2
                                    self.img = OPlayer.plD
                                    self.imgA = OPlayer.plAD
            self.counter += 1




        if self.position == "def":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 953 or self.x < 653 or self.y > 600 or self.y < 220:
                        if self.x > 953 and self.y > 600:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUL
                            self.imgA = OPlayer.plAUL

                        elif self.x > 953 and self.y < 220:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = OPlayer.plDL
                            self.imgA = OPlayer.plADL
                        elif self.x < 653 and self.y > 600:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUR
                            self.imgA = OPlayer.plAUR

                        elif self.x < 653 and self.y < 220:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = OPlayer.plDR
                            self.imgA = OPlayer.plADR

                        elif self.x > 953:
                            self.x = self.x - 2
                            self.img = OPlayer.plL
                            self.imgA = OPlayer.plAL
                        elif self.x < 653:
                            self.x = self.x + 2
                            self.img = OPlayer.plR
                            self.imgA = OPlayer.plAR 
                        elif self.y > 600:
                            self.y = self.y - 2
                            self.img = OPlayer.plU
                            self.imgA = OPlayer.plAU
                        elif self.y < 220:
                            self.y = self.y + 2
                            self.img = OPlayer.plD
                            self.imgA = OPlayer.plAD

                    
                    else:
                        if (ball.x < 653):
                            self.defaultPositionx = 653
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 

                        else:
                            if ball.OgetStuck() == True:
                                self.defaultPositionx = ball.x + 100
                                if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR

                                elif self.x > self.defaultPositionx:
                                    self.x -= 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < self.defaultPositionx:
                                    self.x += 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                            elif ball.OgetStuck() == False:
                                if self.x > ball.x and self.y > ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUL
                                    self.imgA = OPlayer.plAUL

                                elif self.x > ball.x and self.y < ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDL
                                    self.imgA = OPlayer.plADL

                                elif self.x < ball.x and self.y > ball.y:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUR
                                    self.imgA = OPlayer.plAUR

                                elif self.x < ball.x and self.y < ball.y:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDR
                                    self.imgA = OPlayer.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                                elif self.y > ball.y :
                                    self.y = self.y - 2
                                    self.img = OPlayer.plU
                                    self.imgA = OPlayer.plAU
                                elif self.y < ball.y :
                                    self.y = self.y + 2
                                    self.img = OPlayer.plD
                                    self.imgA = OPlayer.plAD
            self.counter += 1



    # Since halftime changes the position of the players, this function applies the Same AI above, 
    # but for the switched postions.

    def HalfTimeTeamMateMovement(self,ball):
      
        if self.position == "gk":
            if self.active == False:

                if self.counter % 2 == 0:
            
                    self.defaultPositionx = 60
                    self.defaultPositiony = 414
                    if self.x > self.defaultPositionx and self.y > self.defaultPositiony:
                        self.x -= 1
                        self.y -= 1
                        self.img = OPlayer.plUL
                        self.imgA = OPlayer.plAUL

                    elif self.x > self.defaultPositionx and self.y < self.defaultPositiony:
                        self.x -= 1
                        self.y += 1
                        self.img = OPlayer.plDL
                        self.imgA = OPlayer.plADL

                    elif self.x < self.defaultPositionx and self.y > self.defaultPositiony:
                        self.x += 1
                        self.y -= 1
                        self.img = OPlayer.plUR
                        self.imgA = OPlayer.plAUR

                    elif self.x < self.defaultPositionx and self.y < self.defaultPositiony:
                        self.x += 1
                        self.y += 1
                        self.img = OPlayer.plDR
                        self.imgA = OPlayer.plADR


                    elif self.x > self.defaultPositionx:
                        self.x -= 1
                        self.img = OPlayer.plL
                        self.imgA = OPlayer.plAL
                    elif self.x < self.defaultPositionx:
                        self.x += 1
                        self.img = OPlayer.plR
                        self.imgA = OPlayer.plAR
                    elif self.y > self.defaultPositiony:
                        self.y -= 1
                        self.img = OPlayer.plU
                        self.imgA = OPlayer.plAU
                    elif self.y < self.defaultPositiony:
                        self.y += 1
                        self.img = OPlayer.plD
                        self.imgA = OPlayer.plAD

                    if self.x == self.defaultPositionx and self.y == self.defaultPositiony:
                        self.img = OPlayer.plR
                        self.imgA = OPlayer.plAR
                        self.counter = 0

            self.counter+= 1


        if self.position == "midUp":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1150 or self.x < 241 or self.y > 200 or self.y < 100:
                        if self.x > 1150 and self.y > 200:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUL
                            self.imgA = OPlayer.plAUL

                        elif self.x > 1150 and self.y < 100:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = OPlayer.plDL
                            self.imgA = OPlayer.plADL
                        elif self.x < 241 and self.y > 200:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUR
                            self.imgA = OPlayer.plAUR

                        elif self.x < 241 and self.y < 100:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = OPlayer.plDR
                            self.imgA = OPlayer.plADR

                        elif self.x > 1150:
                            self.x = self.x - 2
                            self.img = OPlayer.plL
                            self.imgA = OPlayer.plAL
                        elif self.x < 241:
                            self.x = self.x + 2
                            self.img = OPlayer.plR
                            self.imgA = OPlayer.plAR 
                        elif self.y > 200:
                            self.y = self.y - 2
                            self.img = OPlayer.plU
                            self.imgA = OPlayer.plAU
                        elif self.y < 100:
                            self.y = self.y + 2
                            self.img = OPlayer.plD
                            self.imgA = OPlayer.plAD

        
                    else:
                        if (ball.x < 242):
                            self.defaultPositionx = 242
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 

                        elif (ball.x > 951 or ball.x < 241) or (ball.y > 300 or ball.y < 67):
                            self.defaultPositionx = ball.x - 100
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR
                            
                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 
                        else:
                            if ball.OgetStuck() == False:
                                if self.x > ball.x and self.y > ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUL
                                    self.imgA = OPlayer.plAUL

                                elif self.x > ball.x and self.y < ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDL
                                    self.imgA = OPlayer.plADL

                                elif self.x < ball.x and self.y > ball.y + 25:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUR
                                    self.imgA = OPlayer.plAUR

                                elif self.x < ball.x and self.y < ball.y + 25:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDR
                                    self.imgA = OPlayer.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                                elif self.y > ball.y + 25:
                                    self.y = self.y - 2
                                    self.img = OPlayer.plU
                                    self.imgA = OPlayer.plAU
                                elif self.y < ball.y + 25:
                                    self.y = self.y + 2
                                    self.img = OPlayer.plD
                                    self.imgA = OPlayer.plAD

        

            self.counter += 1
                    # If out, go to box and stay relative to ball
                    # If In and ball out stay relative x to ball
                    # If In and ball in and not teammate, go to ball and tackle
    

        if self.position == "midDown": 
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1150 or self.x < 241 or self.y > 800 or self.y < 650:
                        if self.x > 1150 and self.y > 800:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUL
                            self.imgA = OPlayer.plAUL

                        elif self.x > 1150 and self.y < 650:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = OPlayer.plDL
                            self.imgA = OPlayer.plADL
                        elif self.x < 241 and self.y > 800:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUR
                            self.imgA = OPlayer.plAUR

                        elif self.x < 241 and self.y < 650:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = OPlayer.plDR
                            self.imgA = OPlayer.plADR

                        elif self.x > 1150:
                            self.x = self.x - 2
                            self.img = OPlayer.plL
                            self.imgA = OPlayer.plAL
                        elif self.x < 241:
                            self.x = self.x + 2
                            self.img = OPlayer.plR
                            self.imgA = OPlayer.plAR 
                        elif self.y > 800:
                            self.y = self.y - 2
                            self.img = OPlayer.plU
                            self.imgA = OPlayer.plAU
                        elif self.y < 650:
                            self.y = self.y + 2
                            self.img = OPlayer.plD
                            self.imgA = OPlayer.plAD

        
                    else:
                        if (ball.x < 242):
                            self.defaultPositionx = 242
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 

                        elif (ball.x > 951 or ball.x < 241) or (ball.y > 810 or ball.y < 600):
                            self.defaultPositionx = ball.x - 100
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR
                            
                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 
                        else:
                            if ball.OgetStuck() == False:
                                if self.x > ball.x and self.y > ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUL
                                    self.imgA = OPlayer.plAUL

                                elif self.x > ball.x and self.y < ball.y + 25:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDL
                                    self.imgA = OPlayer.plADL

                                elif self.x < ball.x and self.y > ball.y + 25:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUR
                                    self.imgA = OPlayer.plAUR

                                elif self.x < ball.x and self.y < ball.y + 25:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDR
                                    self.imgA = OPlayer.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                                elif self.y > ball.y + 25:
                                    self.y = self.y - 2
                                    self.img = OPlayer.plU
                                    self.imgA = OPlayer.plAU
                                elif self.y < ball.y + 25:
                                    self.y = self.y + 2
                                    self.img = OPlayer.plD
                                    self.imgA = OPlayer.plAD
                   
            self.counter += 1

        if self.position == "att":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 1050 or self.x < 380 or self.y > 600 or self.y < 300:
                        if self.x > 1150 and self.y > 600:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUL
                            self.imgA = OPlayer.plAUL

                        elif self.x > 1050 and self.y < 300:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = OPlayer.plDL
                            self.imgA = OPlayer.plADL
                        elif self.x < 380 and self.y > 600:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUR
                            self.imgA = OPlayer.plAUR

                        elif self.x < 380 and self.y < 300:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = OPlayer.plDR
                            self.imgA = OPlayer.plADR

                        elif self.x > 1050:
                            self.x = self.x - 2
                            self.img = OPlayer.plL
                            self.imgA = OPlayer.plAL
                        elif self.x < 380:
                            self.x = self.x + 2
                            self.img = OPlayer.plR
                            self.imgA = OPlayer.plAR 
                        elif self.y > 600:
                            self.y = self.y - 2
                            self.img = OPlayer.plU
                            self.imgA = OPlayer.plAU
                        elif self.y < 300:
                            self.y = self.y + 2
                            self.img = OPlayer.plD
                            self.imgA = OPlayer.plAD

                    
                    else:

                        if (ball.x < 380):
                            self.defaultPositionx = 380
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 

                        else:
                            if ball.OgetStuck() == True: #ball.x > 1050 or ball.x < 380) or (ball.y > 300 or ball.y < 600
                                self.defaultPositionx = ball.x - 50
                                if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR
                                
                                elif self.x > self.defaultPositionx:
                                    self.x -= 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < self.defaultPositionx:
                                    self.x += 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                            elif ball.OgetStuck() == False:
                                if self.x > ball.x and self.y > ball.y :
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUL
                                    self.imgA = OPlayer.plAUL

                                elif self.x > ball.x and self.y < ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDL
                                    self.imgA = OPlayer.plADL

                                elif self.x < ball.x and self.y > ball.y:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUR
                                    self.imgA = OPlayer.plAUR

                                elif self.x < ball.x and self.y < ball.y:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDR
                                    self.imgA = OPlayer.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                                elif self.y > ball.y :
                                    self.y = self.y - 2
                                    self.img = OPlayer.plU
                                    self.imgA = OPlayer.plAU
                                elif self.y < ball.y :
                                    self.y = self.y + 2
                                    self.img = OPlayer.plD
                                    self.imgA = OPlayer.plAD
            self.counter += 1



        if self.position == "def":
            if self.active == False:
                if self.counter % 2 == 0:
                    if self.x > 451 or self.x < 250 or self.y > 600 or self.y < 220:
                        if self.x > 451 and self.y > 600:
                            self.x = self.x - 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUL
                            self.imgA = OPlayer.plAUL

                        elif self.x > 451 and self.y < 220:
                            self.x = self.x - 2
                            self.y = self.y + 2
                            self.img = OPlayer.plDL
                            self.imgA = OPlayer.plADL
                        elif self.x < 250 and self.y > 600:
                            self.x = self.x + 2
                            self.y = self.y - 2
                            self.img = OPlayer.plUR
                            self.imgA = OPlayer.plAUR

                        elif self.x < 250 and self.y < 220:
                            self.x = self.x + 2  
                            self.y = self.y + 2
                            self.img = OPlayer.plDR
                            self.imgA = OPlayer.plADR

                        elif self.x > 451:
                            self.x = self.x - 2
                            self.img = OPlayer.plL
                            self.imgA = OPlayer.plAL
                        elif self.x < 250:
                            self.x = self.x + 2
                            self.img = OPlayer.plR
                            self.imgA = OPlayer.plAR 
                        elif self.y > 600:
                            self.y = self.y - 2
                            self.img = OPlayer.plU
                            self.imgA = OPlayer.plAU
                        elif self.y < 220:
                            self.y = self.y + 2
                            self.img = OPlayer.plD
                            self.imgA = OPlayer.plAD

                    
                    else:
                        if (ball.x >=451):
                            self.defaultPositionx = 451
                            if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR

                            elif self.x > self.defaultPositionx:
                                self.x -= 2
                                self.img = OPlayer.plL
                                self.imgA = OPlayer.plAL

                            elif self.x < self.defaultPositionx:
                                self.x += 2
                                self.img = OPlayer.plR
                                self.imgA = OPlayer.plAR 

                        else:
                            if ball.OgetStuck() == True:
                                self.defaultPositionx = ball.x - 100
                                if self.x == self.defaultPositionx+1 or self.x == self.defaultPositionx:
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR

                                elif self.x > self.defaultPositionx:
                                    self.x -= 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < self.defaultPositionx:
                                    self.x += 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                            elif ball.OgetStuck() == False:
                                if self.x > ball.x and self.y > ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUL
                                    self.imgA = OPlayer.plAUL

                                elif self.x > ball.x and self.y < ball.y:
                                    self.x = self.x - 2
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDL
                                    self.imgA = OPlayer.plADL

                                elif self.x < ball.x and self.y > ball.y:
                                    self.x = self.x + 2
                                    self.y = self.y - 2
                                    self.img = OPlayer.plUR
                                    self.imgA = OPlayer.plAUR

                                elif self.x < ball.x and self.y < ball.y:
                                    self.x = self.x + 2  
                                    self.y = self.y + 2
                                    self.img = OPlayer.plDR
                                    self.imgA = OPlayer.plADR

                                elif self.x > ball.x :
                                    self.x = self.x - 2
                                    self.img = OPlayer.plL
                                    self.imgA = OPlayer.plAL

                                elif self.x < ball.x :
                                    self.x = self.x + 2
                                    self.img = OPlayer.plR
                                    self.imgA = OPlayer.plAR 

                                elif self.y > ball.y :
                                    self.y = self.y - 2
                                    self.img = OPlayer.plU
                                    self.imgA = OPlayer.plAU
                                elif self.y < ball.y :
                                    self.y = self.y + 2
                                    self.img = OPlayer.plD
                                    self.imgA = OPlayer.plAD
            self.counter += 1




    # Function used to move the player from user controls.
    # The y and x lower and upper limits are the boundaries of the field.

    # The variable direction which is passed in is which way the user wishes the player to go
    
    # The function also has img and imgA from each direction, which updates the picture based 
    # on the direction the player is going


    def Move(self,direction):
    # Movement function with acceleration 
        if direction == 'UP' and self.y > self.yupperLimit:
            self.y -= self.velocity
            self.img = self.plU
            self.imgA = self.plAU
                
        elif direction == 'DOWN' and self.y <= self.ylowerLimit:
            self.y += self.velocity           
            self.img = self.plD
            self.imgA = self.plAD
                    
        elif direction == 'LEFT' and self.x > self.xupperLimit:
            self.x -= self.velocity
            self.img = self.plL
            self.imgA = self.plAL

        elif direction == 'RIGHT' and self.x <= self.xlowerLimit:
            self.x += self.velocity
            self.img = self.plR
            self.imgA = self.plAR

        elif direction == 'UPLEFT' and self.y > self.yupperLimit and self.x > self.xupperLimit:
            self.y -= self.velocity
            self.x -= self.velocity
            self.img = self.plUL
            self.imgA = self.plAUL

        elif direction == 'UPRIGHT' and self.y > self.yupperLimit and self.x <= self.xlowerLimit:
            self.y -= self.velocity
            self.x += self.velocity
            self.img = self.plUR
            self.imgA = self.plAUR

        elif direction == 'DOWNLEFT' and self.y <= self.ylowerLimit and self.x > self.xupperLimit:
            self.y += self.velocity
            self.x -= self.velocity
            self.img = self.plDL
            self.imgA = self.plADL

        elif direction == 'DOWNRIGHT' and self.y <= self.ylowerLimit and self.x <= self.xlowerLimit:
            self.y += self.velocity
            self.x += self.velocity
            self.img = self.plDR
            self.imgA = self.plADR




# The soccer ball class
class Ball():

    ball = pygame.image.load("Images/Soccer-Ball-icon.png")
    # load up the ball


    def __init__(self):
        self.stick = False
        self.Ostick = False
        self.x = 573
        self.y = 427
        self.xvelocity = 6
        self.yvelocity = 6
        self.xBounceOnce = False
        self.yBounceOnce = False
        self.count = 0
        self.direction = ''
        self.leftGoal = False
        self.rightGoal = False
        # iniitialise the variables for the ball
        # x and y of the ball,
        # xvelocity and y velocity is how fast it travels when kicked
        # xbounce and ybounce check if it has bounced on an edge 
    
    def setxy(self,x,y):
        self.x = x
        self.y = y

    #set ball x and y

    # Get Stuck if it is touched by player from blue team
    def getStuck(self):
        return self.stick

    # we can also set this
    def setStuck(self,boolean):
        self.stick = boolean

    # Get Stuck if it is touched by player from Red team
    def OgetStuck(self):
        return self.Ostick

    # we can also set this
    def OsetStuck(self,boolean):
        self.Ostick = boolean

    #move in relation to player
    # aka dribble position of the ball
    # direction is which way player is going
    def StickWith(self,player,direction):
        if direction == 'UP':
            self.x = player.x + 13
            self.y = player.y - 20

        elif direction == "":
            pass

        elif direction == 'DOWN':
            self.x = player.x + 13
            self.y = player.y + 45
    
        elif direction == 'LEFT':
            self.x = player.x - 20
            self.y = player.y + 13

        elif direction == 'RIGHT':
            self.x = player.x + 45
            self.y = player.y + 13

        elif direction == 'UPLEFT':
            self.x = player.x - 9
            self.y = player.y - 9

        elif direction == 'UPRIGHT':
            self.x = player.x + 38
            self.y = player.y - 7

        elif direction == 'DOWNLEFT':
            self.x = player.x - 9
            self.y = player.y + 34

        elif direction == 'DOWNRIGHT':
            self.x = player.x + 36
            self.y = player.y + 35



    #Check if touching a specific player based on x and y values
    def collideWith(self,player):
        if player.x <= self.x:
            if abs(self.x - player.x) <= 45 and abs(self.y - player.y) <= 25: 
                return True
        elif player.x > self.x:
            if abs(self.x - player.x) <= 25 and abs(self.y - player.y) <= 25: 
                return True



    #Draw Image, blit to screen
    def draw(self):
        screen.blit(self.ball,(self.x,self.y))

    #Update image on pass
    def Move(self,command):
    # Returning false means ball is still moving
    # Returning True means ball is done moving


        if self.count == 0:
            self.direction = command

        if self.direction == 'UP':
            self.y = self.y - self.yvelocity  
        elif self.direction == "":
            pass
        elif self.direction == 'DOWN':
            self.y = self.y + self.yvelocity  
    
        elif self.direction == 'LEFT':
            self.x = self.x - self.xvelocity  

        elif self.direction == 'RIGHT':
            self.x = self.x  + self.xvelocity  

        elif self.direction == 'UPLEFT':
            self.x = self.x - self.xvelocity  
            self.y = self.y - self.yvelocity 
 
        elif self.direction == 'UPRIGHT':
            self.x = self.x + self.xvelocity
            self.y = self.y - self.yvelocity

        elif self.direction == 'DOWNLEFT':
            self.x = self.x - self.xvelocity
            self.y = self.y + self.yvelocity

        elif self.direction == 'DOWNRIGHT':
            self.x = self.x + self.xvelocity
            self.y = self.y + self.yvelocity

        if self.x > 1130 or self.x < 43:
            # These boundaries ^^ are the boundaries of the field
            if self.x >= 0 and self.x < 10 and self.y > 340 and self.y < 520:
                # These boundaries are boundaries of the left goal ^^
                self.xvelocity = 0
                self.yvelocity = 0
                self.leftGoal = True
                return True
                #stop if it hits the walls of the nets 


            if self.x >= 1175 and self.x < 1200 and self.y > 340 and self.y < 520:
                # These boundaries are boundaries of the right goal ^^

                self.xvelocity = 0
                self.yvelocity = 0
                self.rightGoal = True
                return True
                #stop if it hits the walls of the nets 

            if self.x > 0 and self.x < 43 and self.y > 340 and self.y < 520:
                pass
            elif self.y > 340 and self.y < 520:
                pass

            elif self.xBounceOnce == False:
                self.xvelocity = -1*self.xvelocity
                self.xBounceOnce = True
                #Bounce of boundaries of wall by settting x-velocity negative
            else:
                pass



        if self.y > 790 or self.y < 65:
            if self.yBounceOnce == False:
                self.yvelocity = -1*self.yvelocity
                self.yBounceOnce = True
            #Bounce of boundaries of wall by settting y-velocity negative


        if self.count > 20: # aka ball stop moving
        # after 20 counts, stop the ball. 

            if self.x > 0 and self.x < 43 and self.y > 340 and self.y < 520:
                self.leftGoal = True
                return True
            # check if goal scored
            if self.x > 1130 or self.x < 43 and self.y > 340 and self.y < 520:
                self.rightGoal = True
                return True

            #set velocity to default 6 again
            self.yvelocity = 6
            self.xvelocity = 6
            self.xBounceOnce = False
            self.yBounceOnce = False
            self.count = 0
            return True

        self.count = self.count + 1
        return False


    # calculate the distance to the player from the ball using distance formula
    def CalcDistance(self,player):
        fullDistance = abs(((self.y - player.y)**2) + ((self.x - player.x)**2))**.5
        return fullDistance
     


# Pause screen for the pause function
def Pause():
    PauseFont = pygame.font.SysFont("monospace", 70)
    pauseText =  PauseFont.render("Game Paused", True, (0, 0, 0))
    continueText = PauseFont.render("Press P to Continue", True, (0, 0, 0))
    quitText = PauseFont.render("Press Q to Quit", True, (0, 0, 0))

    screen.fill((255,255,255))
    pause = False

    while not pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pause = True
                    sys.exit()
                if event.key == pygame.K_p:
                    pause = True

                #Quit by q, or continue by ending while loop with P

        screen.fill((244,244,244))
        screen.blit(pauseText,(360,200))
        screen.blit(continueText,(210,400))
        screen.blit(quitText,(290,600))

        # Blit the text to the screen


        pygame.display.update()
        clock.tick(30)



# Halftime Function
def HalfTime(score1,score2,totalPasses1,totalPasses2):

    HalfTimeFont = pygame.font.SysFont("monospace", 70)
    halfTimeText =   HalfTimeFont.render("Half Time", True, (0, 0, 0))
    totalPassesText =  HalfTimeFont.render("Blue Team Passes: " + str(totalPasses1), True, (0, 0, 0))
    OtotalPassesText = HalfTimeFont.render("Red Team Passes: " + str(totalPasses2), True, (0, 0, 0))
    scoreText = HalfTimeFont.render("Score:" + str(score1) + "-" + str(score2), True, (0, 0, 0))
    rageQuitText = HalfTimeFont.render("Press Q to Quit", True, (0, 0, 0))
    continueText = HalfTimeFont.render("Press Space to Continue", True, (0, 0, 0))

    # Display Halftime stats, like total passes and goals scored by either team

    screen.fill((255,255,255))
    pause = False

    while not pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pause = True
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    pause = True


        screen.fill((244,244,244))
        screen.blit(halfTimeText,(400,100))
        screen.blit(totalPassesText,(200,200))
        screen.blit(OtotalPassesText,(200,300))
        screen.blit(scoreText,(410,400))
        screen.blit(rageQuitText,(290,520))
        screen.blit(continueText,(120,600))

        #Blit the text to the screen


        pygame.display.update()
        clock.tick(30)

def GameDoneScreen(score1,score2,totalPasses1,totalPasses2):
    # Screen before ending the game

    #global multiDone to end the main game loop
    global multiDone
    gameDone = False

    FullTimeFont = pygame.font.SysFont("monospace", 70)
    FullTimeText =   FullTimeFont.render("Game Over", True, (0, 0, 0))
    totalPassesText =  FullTimeFont.render("Blue Team Passes: " + str(totalPasses1), True, (0, 0, 0))
    OtotalPassesText = FullTimeFont.render("Red Team Passes: " + str(totalPasses2), True, (0, 0, 0))
    scoreText = FullTimeFont.render("Score:" + str(score1) + "-" + str(score2), True, (0, 0, 0))
    rageQuitText = FullTimeFont.render("Press Q to Quit", True, (0, 0, 0))
    continueText = FullTimeFont.render("Press Space to Exit", True, (0, 0, 0))
  
    if score1 > score2:
        maximumScore = score1
    else:
        maximumScore = score2

    newFile = open("HighScores.txt","a")
    newFile.write(str(maximumScore))
    newFile.write("\n")
    newFile.close()

    while not gameDone:
        screen.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameDone = True
                    sys.exit()

                if event.key == pygame.K_SPACE:
                    gameDone = True
                    multiDone = True

                # End loop with space, quit game with q

        screen.fill((244,244,244))
        screen.blit(FullTimeText,(400,100))
        screen.blit(totalPassesText,(200,200))
        screen.blit(OtotalPassesText,(200,300))
        screen.blit(scoreText,(410,400))
        screen.blit(rageQuitText,(290,520))
        screen.blit(continueText,(200,600))


        # Blit text to the screen
        pygame.display.update()
        clock.tick(30)

def HelpScreen():
    # Help screen from the main menu


    help = False
    while not help:
        screen.blit(helpMenu,(0,0))
        # blit the help screen image


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    help = True
                    sys.exit()
                if event.key == pygame.K_SPACE:
                    help = True
                # Continue with space, quit with q

        pygame.display.update()
        clock.tick(30)


def Multiplayer():


    # The main function for multiplayer mode

    ########## VARIABLES ##########
    #False are set for future keyboard useage
    size = (1200, 820)
    animateBall = False # whether ball is moving on blue team
    OanimateBall = False # whether ball is moving on red team
    xPress = False #wheter x is pressed
    passPress = False # whether / is pressed
    multiDone = False # Main game loop boolean
    totalSeconds = 0 # Time since start
    frameCount = 0 # Total frame count
    frameRate = 60 # Frame Rate
    totalPasses = 0 # Blue team total passes
    OtotalPasses = 0 # Red team total passes
    halfTimeOver = False #Wheter halftime is over

    clock = pygame.time.Clock()
    #pygame clock






    #####################################################
    #instantiate players below.  

    ## LEFT SIDE TEAM ################
    attPlayer1 = player(419,414,2,'att',True)
    midPlayerUp = player(300,154,2,'midUp')
    midPlayerDown = player(300,654,2,'midDown')
    defPlayer1 = player(241,414,2,'def')
    keeperPlayer = player(60,414,1,'gk')
    # first 2 variables are x,y position
    # 2 and 1 is the speed,
    # True indicates to start the user on that player




    ### RIGHT SIDE TEAM, O stands for opponent ##############
    OattPlayer1 = OPlayer(701,414,2,'att',True)
    OmidPlayerUp = OPlayer(830,154, 2, 'midUp')
    OmidPlayerDown = OPlayer(830,654, 2, 'midDown')
    OdefPlayer1 = OPlayer(890,419,2,'def')
    OkeeperPlayer = OPlayer(1090,414, 1, 'gk')

    # first 2 variables are x,y position
    # 2 and 1 is the speed,
    # True indicates to start the user on that player


    #Main ball object
    ball = Ball()


    listOfPlayers = [attPlayer1,midPlayerUp,midPlayerDown,defPlayer1,keeperPlayer]
        # list of blue team ^^ players and red team (below) players
    OlistOfPlayers = [OattPlayer1,OmidPlayerUp,OmidPlayerDown,OdefPlayer1,OkeeperPlayer]


    #Index counter from the lists above
    currentIndex = 0    
    OcurrentIndex = 0


    commander = ''
    Ocommander = ''
    #strings that contain the direction


    #Game font
    font = pygame.font.SysFont("monospace", 35)

    #Game info text on the top
    score = font.render("Score: 0-0", True, (255, 255, 255))
    timeLeft = font.render("Time Left:", True, (255, 255, 255))
    PressP = font.render("Press P to Pause", True, (255, 255, 255))
    scoreLeft = 0
    scoreRight = 0
    #Team scores variables


    #Time for each half
    halfTimeTime = 100
    halfTimeCounter = 0
    #halftime counter counts how many haltimes have passed, basically 0 or 1, and 2 when game over

    #############################################
    #############################

    while not multiDone:
#main game loop
        
        totalSeconds = frameCount/frameRate
        # Used to  calculate time passed


        # time display on top
        time = font.render(str(halfTimeTime-totalSeconds), True, (255, 255, 255))
        #score display on top
        score = font.render("Score:" + str(scoreLeft) +'-' + str(scoreRight), True, (255, 255, 255))

        keyW = False
        keyA = False
        keyS = False
        keyD = False
        keyWA = False
        keyWD = False
        keySA = False
        keySD = False
        xPress = False
        passPress = False
        # KEYBOARED PRESSED OR NOT VARIABLES
        keyAup = False
        keyAleft = False
        keyAdown = False
        keyAright = False
        keyAupleft = False
        keyAupright = False
        keyAdownleft = False
        keyAdownright = False
        controlPress = False
        slashPress = False


        # BLIT INFO FOR THE TOP
        screen.fill((88,88,88))
        screen.blit(bg, [0, 56])
        screen.blit(score, (473,7))
        screen.blit(timeLeft, (890,7))
        screen.blit(time,(1112,7))
        screen.blit(PressP,(20,7))

        keys = pygame.key.get_pressed() # GET KEYS


        # SET KEYS PRESSED VARIABLES TRUE IF THOSE KEYS WERE PRESSED


        if (keys[K_a] and keys[K_w]):
            keyWA = True
        elif (keys[K_d] and keys[K_w]):
            keyWD = True
        elif (keys[K_a] and keys[K_s]):
            keySA = True
        elif (keys[K_d] and keys[K_s]):
            keySD = True

        elif (keys[K_w]):
            keyW = True
        elif (keys[K_d]):
            keyD = True
        elif (keys[K_s]):
            keyS = True
        elif (keys[K_a]):
            keyA = True

        #######################

        if (keys[K_LEFT] and keys[K_UP]):
            keyAupleft = True
        elif (keys[K_RIGHT] and keys[K_UP]):
            keyAupright = True
        elif (keys[K_LEFT] and keys[K_DOWN]):
            keyAdownleft = True
        elif (keys[K_RIGHT] and keys[K_DOWN]):
            keyAdownright = True

        elif (keys[K_UP]):
            keyAup = True
        elif (keys[K_RIGHT]):
            keyAright = True
        elif (keys[K_DOWN]):
            keyAdown = True
        elif (keys[K_LEFT]):
            keyAleft = True


        #######################




        # If those keys were pressed, use the move function for the player
        # access which player to move from the listOfPlayers function
        # use the current index to know which player

        if keyWA == True:
            listOfPlayers[currentIndex].Move('UPLEFT')
            commander = 'UPLEFT'
        elif keyWD == True:
            listOfPlayers[currentIndex].Move('UPRIGHT')
            commander = 'UPRIGHT'
        elif keySA == True:
            listOfPlayers[currentIndex].Move('DOWNLEFT')
            commander = 'DOWNLEFT'
        elif keySD == True:
            listOfPlayers[currentIndex].Move('DOWNRIGHT')
            commander = 'DOWNRIGHT'
        elif keyA == True:
            listOfPlayers[currentIndex].Move('LEFT')
            commander = 'LEFT'
        elif keyD == True:
            listOfPlayers[currentIndex].Move('RIGHT')
            commander = 'RIGHT'
        elif keyW == True:
            listOfPlayers[currentIndex].Move('UP')
            commander = 'UP'
        elif keyS == True:
            listOfPlayers[currentIndex].Move('DOWN')
            commander = 'DOWN'

        # red team below
        if keyAup == True:
            OlistOfPlayers[OcurrentIndex].Move('UP')
            Ocommander = 'UP'
        elif keyAleft == True:
            OlistOfPlayers[OcurrentIndex].Move('LEFT')
            Ocommander = 'LEFT'
        elif keyAdown == True:
            OlistOfPlayers[OcurrentIndex].Move('DOWN')
            Ocommander = 'DOWN'
        elif keyAright == True:
            OlistOfPlayers[OcurrentIndex].Move('RIGHT')
            Ocommander = 'RIGHT'
        elif keyAupleft == True:
            OlistOfPlayers[OcurrentIndex].Move('UPLEFT')
            Ocommander = 'UPLEFT'
        elif keyAupright == True:
            OlistOfPlayers[OcurrentIndex].Move('UPRIGHT')
            Ocommander = 'UPRIGHT'
        elif keyAdownleft == True:
            OlistOfPlayers[OcurrentIndex].Move('DOWNLEFT')
            Ocommander = 'DOWNLEFT'
        elif keyAdownright == True:
            OlistOfPlayers[OcurrentIndex].Move('DOWNRIGHT')
            Ocommander = 'DOWNRIGHT'



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x: # change player
                    if ball.getStuck() == False:
                        xPress = True
                if event.key == pygame.K_h: # to pass press h
                    if ball.getStuck() == True: #can only pass if you have the ball
                        animateBall = True
                        ball.setStuck(False) # unstuck the ball from player on pass

                if event.key == pygame.K_SLASH: # change player
                    if ball.OgetStuck() == False: 
                        slashPress = True
                if event.key == pygame.K_RCTRL:
                    if ball.OgetStuck() == True:#can only pass if you have the ball
                        OanimateBall = True
                        ball.OsetStuck(False)# unstuck the ball from player on pass

                if event.key == pygame.K_p:
                    Pause() # pause game function

        if animateBall == True:
            # move ball from blue team
            if ball.Move(commander) == True:
                animateBall = False
            ball.setStuck(False)

        if OanimateBall == True:
            # move ball from red team
            if ball.Move(Ocommander) == True:
                OanimateBall = False
            ball.OsetStuck(False)

        #If any Player collides with ball, find out and make it current index
        if ball.getStuck() == False:
            for i in range(len(listOfPlayers)):
                if ball.collideWith(listOfPlayers[i]) and ball.getStuck() == False and animateBall == False:
                    ball.setStuck(True)
                    ball.OsetStuck(False)
                    stuckOnIndex = i
        # ^^ If player collides with ball and the ball isnt stuck on a player, stick it to player

        #change ball x,y according to stucked player
        if ball.getStuck() == True:
            ball.StickWith(listOfPlayers[stuckOnIndex],commander)
            listOfPlayers[currentIndex].deActivate()
            listOfPlayers[stuckOnIndex].Activate()
            currentIndex = stuckOnIndex


        # do same check as above, but for red team
        if ball.OgetStuck() == False:
            for i in range(len(OlistOfPlayers)):
                if ball.collideWith(OlistOfPlayers[i]) and ball.OgetStuck() == False and OanimateBall == False:
                    ball.OsetStuck(True)
                    ball.setStuck(False)
                    OstuckOnIndex = i
        # ^^ If player collides with ball and the ball isnt stuck on a player, stick it to player

        #change ball x,y according to stucked player
        if ball.OgetStuck() == True:
            ball.StickWith(OlistOfPlayers[OstuckOnIndex],Ocommander)
            OlistOfPlayers[OcurrentIndex].deActivate()
            OlistOfPlayers[OstuckOnIndex].Activate()
            OcurrentIndex = OstuckOnIndex

        if xPress == True:
            # Go To Next Player
            #This function tries to find the player closest to ball
            #uses function CalcDistance from ball class to get this
            #if current player is closest, choose another player in index
            totalPasses = totalPasses + 1
            listOfPlayers[currentIndex].deActivate()
            minimumDistance = 999999999999

            for i in range(len(listOfPlayers)):
                distanceFromBall = ball.CalcDistance(listOfPlayers[i])
                if distanceFromBall < minimumDistance:
                    minimumDistance = distanceFromBall
                    minimumDistanceIndex = i

            if minimumDistanceIndex == currentIndex:
                if currentIndex == len(listOfPlayers) - 1:
                    currentIndex = 0
                else:
                    currentIndex += 1

                listOfPlayers[currentIndex].Activate()
            else:
                currentIndex = minimumDistanceIndex
                listOfPlayers[currentIndex].Activate()



        if slashPress == True:
            # Duplicate of previous function, but for red team
            OtotalPasses = OtotalPasses + 1
            OlistOfPlayers[OcurrentIndex].deActivate()
            OminimumDistance = 999999999999 # used to comapre to find min distance from ball

            for i in range(len(OlistOfPlayers)):
                OdistanceFromBall = ball.CalcDistance(OlistOfPlayers[i])
                if OdistanceFromBall < OminimumDistance:
                    OminimumDistance = OdistanceFromBall
                    OminimumDistanceIndex = i

            if OminimumDistanceIndex == OcurrentIndex:
                if OcurrentIndex == len(OlistOfPlayers) - 1:
                    OcurrentIndex = 0
                else:
                    OcurrentIndex += 1

                OlistOfPlayers[OcurrentIndex].Activate()
            else:
                OcurrentIndex = OminimumDistanceIndex
                OlistOfPlayers[OcurrentIndex].Activate()




        if halfTimeCounter == 0: # if halftime is not over, change x and y of players based on AI commands
        # from AI movement function of the player

            keeperPlayer.TeamMateMovement(ball)
            midPlayerUp.TeamMateMovement(ball)
            midPlayerDown.TeamMateMovement(ball)
            attPlayer1.TeamMateMovement(ball)
            defPlayer1.TeamMateMovement(ball)
            

            OkeeperPlayer.TeamMateMovement(ball)
            OmidPlayerUp.TeamMateMovement(ball)
            OmidPlayerDown.TeamMateMovement(ball)
            OattPlayer1.TeamMateMovement(ball)
            OdefPlayer1.TeamMateMovement(ball)
     


        if halfTimeCounter == 1:
            #Switch the function based on if halftime is over and player positions are switched
            keeperPlayer.HalfTimeTeamMateMovement(ball)
            midPlayerUp.HalfTimeTeamMateMovement(ball)
            midPlayerDown.HalfTimeTeamMateMovement(ball)
            attPlayer1.HalfTimeTeamMateMovement(ball)
            defPlayer1.HalfTimeTeamMateMovement(ball)
            

            OkeeperPlayer.HalfTimeTeamMateMovement(ball)
            OmidPlayerUp.HalfTimeTeamMateMovement(ball)
            OmidPlayerDown.HalfTimeTeamMateMovement(ball)
            OattPlayer1.HalfTimeTeamMateMovement(ball)
            OdefPlayer1.HalfTimeTeamMateMovement(ball)




        ball.draw()
        attPlayer1.draw()
        midPlayerUp.draw()
        midPlayerDown.draw()
        defPlayer1.draw()
        keeperPlayer.draw()
        #draw em all
        OattPlayer1.draw()
        OmidPlayerUp.draw()
        OmidPlayerDown.draw()
        OdefPlayer1.draw()
        OkeeperPlayer.draw()



        # aka if halftime comes
        if totalSeconds == halfTimeTime and halfTimeOver == False:
            halfTimeOver = True
            halfTimeCounter += 1 
            if halfTimeCounter == 2: # if second time that time runs out, go to endgame screen
                GameDoneScreen(scoreLeft,scoreRight,totalPasses,OtotalPasses)
                multiDone = True
            

            if halfTimeCounter == 1: # if first time time runs out, go to halftime screen
                HalfTime(scoreLeft,scoreRight,totalPasses,OtotalPasses)
                totalSeconds = 0
                # reset time
                

                # reset player positions to opposite sides
                attPlayer1.setxy(701,414, True)
                midPlayerUp.setxy(830,154, False)
                midPlayerDown.setxy(830,654, False)
                defPlayer1.setxy(890,414, False)
                keeperPlayer.setxy(1090,414, False)

                OattPlayer1.setxy(419,414, True)
                OmidPlayerUp.setxy(300,154, False)
                OmidPlayerDown.setxy(300,654, False)
                OdefPlayer1.setxy(241,414, False)
                OkeeperPlayer.setxy(60,414, False)
                frameCount = 0 #reset frames (for time counting reasons)
                halfTimeOver = False
                ball.stick = False 
                ball.Ostick = False
                #stop sticking to players and set ball to initial position
                ball.setxy(573,427)




        if ball.leftGoal == True:
            pygame.time.wait(1000)

            # Then reset players, based on whether halftime passed or not
            if halfTimeCounter == 1:
                attPlayer1.setxy(701,414, True)
                midPlayerUp.setxy(830,154, False)
                midPlayerDown.setxy(830,654, False)
                defPlayer1.setxy(890,414, False)
                keeperPlayer.setxy(1090,414, False)
                OattPlayer1.setxy(419,414, True)
                OmidPlayerUp.setxy(300,154, False)
                OmidPlayerDown.setxy(300,654, False)
                OdefPlayer1.setxy(241,414, False)
                OkeeperPlayer.setxy(60,414, False)
                ball.stick = False
                ball.Ostick = False
                ball.setxy(573,427)
                scoreLeft += 1
                ball.leftGoal = False #switch which side is goal @ halftime

            else:
                OattPlayer1.setxy(701,414, True)
                OmidPlayerUp.setxy(830,154, False)
                OmidPlayerDown.setxy(830,654, False)
                OdefPlayer1.setxy(890,414, False)
                OkeeperPlayer.setxy(1090,414, False)
                attPlayer1.setxy(419,414, True)
                midPlayerUp.setxy(300,154, False)
                midPlayerDown.setxy(300,654, False)
                defPlayer1.setxy(241,414, False)
                keeperPlayer.setxy(60,414, False)
                ball.stick = False
                ball.Ostick = False
                ball.setxy(573,427)
                scoreRight += 1 # if goal scored, count it to variable,
                ball.leftGoal = False

        if ball.rightGoal == True:
            pygame.time.wait(1000)

            # Then reset players, based on whether halftime passed or not
            if halfTimeCounter == 1:
                attPlayer1.setxy(701,414, True)
                midPlayerUp.setxy(830,154, False)
                midPlayerDown.setxy(830,654, False)
                defPlayer1.setxy(890,414, False)
                keeperPlayer.setxy(1090,414, False)
                OattPlayer1.setxy(419,414, True)
                OmidPlayerUp.setxy(300,154, False)
                OmidPlayerDown.setxy(300,654, False)
                OdefPlayer1.setxy(241,414, False)
                OkeeperPlayer.setxy(60,414, False)
                ball.stick = False
                ball.Ostick = False
                ball.setxy(573,427)
                scoreRight+=1      # switch which side at halftime 
                ball.rightGoal = False

            else:
                OattPlayer1.setxy(701,414, True)
                OmidPlayerUp.setxy(830,154, False)
                OmidPlayerDown.setxy(830,654, False)
                OdefPlayer1.setxy(890,414, False)
                OkeeperPlayer.setxy(1090,414, False)
                attPlayer1.setxy(419,414, True)
                midPlayerUp.setxy(300,154, False)
                midPlayerDown.setxy(300,654, False)
                defPlayer1.setxy(241,414, False)
                keeperPlayer.setxy(60,414, False)
                ball.stick = False
                ball.Ostick = False
                ball.setxy(573,427)
                scoreLeft += 1            # if goal scored, count it to variable,
                ball.rightGoal = False


        pygame.display.update()
        frameCount += 1
        clock.tick(frameRate)

def findHighScore():
    HSFile = open("HighScores.txt","r")
    maximum = 0
    line = HSFile.readline().strip()
    while line:
        if int(line) > maximum:
            maximum = int(line)
        line = HSFile.readline().strip()
    HSFile.close()
    return maximum


######### SET UP ############
pygame.init()
size = (1200, 820) # window size
pygame.display.set_caption('FIFO 16')
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
##########################################
bg = pygame.image.load("Images/ground.png").convert()
menu = pygame.image.load("Images/Menu.png").convert()
helpMenu = pygame.image.load("Images/Help.png").convert()
#####################################################
MenuFont = pygame.font.SysFont("monospace", 30) # initialize font for high score 

menuNow = False
##### MENU ############

# main menu loop
while not menuNow:
    highScore = findHighScore() # call function to find high score
    menuHighScoreText = MenuFont.render("High Score: " + str(highScore) + " goals", True, (255, 255, 255)) #redner the text 

    screen.blit(menu, [0, 0])     # blit menu image
    screen.blit(menuHighScoreText,(180,780)) # blit high score to main menu

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                menuNow = True
                sys.exit()
            if event.key == pygame.K_SPACE:
                Multiplayer()
                # press space to start
            if event.key == pygame.K_h:
                HelpScreen()
                # press h for help
   
    
    pygame.display.update()        
    clock.tick(50)

sys.exit()
