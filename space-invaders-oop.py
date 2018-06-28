#Importing required modules
import pygame
import random

#Defining RGB values for colours
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
TITLE_WHITE = ( 255, 200, 255)
LIGHT_GREEN = (0, 180, 0)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)


# adding font file
FONT = "fonts/space_invaders.ttf"

#List to store enemy ships
ships = [
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1]
]

#Initialzing high score from text file "highscore.txt"
try:
    filename = "highscore.txt"
    file = open(filename,"r")
    highest_score = int(file.read())
    if highest_score == ' ':
        highest_score=0
    file.close()
except:
    highest_score=0

class Ship(pygame.sprite.Sprite):
    """
    Defining the defender spaceship and its
    properties
    """

    # defines the initial x and y pos of our ship
    def __init__(self, x_pos, y_pos):
        sprite.Sprite.__init__()

        self.image = pygame.image.load("ship.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (x_pos, y_pos))

        self.moving_speed = 4

    # defines the left movement
    def left(self):
        if self.rect.x > 20:
            self.rect.x -= self.moving_speed
            game.screen.blit(self.image, self.rect)

    # defines the right movement
    def right(self):
        if self.rect.x < 780:
            self.rect.x += self.moving_speed
            game.screen.blit(self.image, self.rect)

    # defines the shooting
    def shoot(self):
        Missile.shoot() # missile is another class
                        # not sure, still

class Bullet(pygame.sprite.Sprite):
    """
    describing bullets; thinking to keep missils
    type same for everythnig - all alien ships and
    defender
    """
    def __init__(self, image_missile, x_pos, y_pos, direction, speed):
        
        super().__init__()
        self.image = image_missile
        self.rect = self.image.get_rect(topleft = (x_pos, y_pos))
        self.direction = direction
        self.speed = speed
        
    #def shoot(self):
        # if it goes beyond certain dimension, self.kill()
        # self.rect.y += self.speed * self.direction

        
class Enemy(pygame.sprite.Sprite):
    """
    class for alien spaceship and their
    properties. We need to create a list of
    lists of objects of this class Aliens probably.
    """
    def __init__(self, ships, alien_image, x_pos, y_pos):
        super().__init__()
        
        self.image = alien_image
        self.rect = self.image.get_rect(topleft = (x_pos, y_pos)) 
            
    #def move_down(self, movement):
        # to make the ship come down
        
    #def move_horizontal(self, movement): 
        # to make ship oscilate horizontally
        
    #def shoot(self):
        # not all ships will shoot at once, we need to randomly select some of them
        # and call the Missile.shoot function or something to make them shoot


class Blocker(pygame.sprite.Sprite):
    """
    Class for defining blocks and their properties;
    basically their damage rate.
    """
    def __init__(self, block_image):
        super().__init__()
        self.image = block_image
        self.rect = self.image.get_rect()
        # or probably, just a simple rectangle object.
        # for i in range(self.height):
        #     for j in range(self.width):
        #         pygame.draw.rect(display, self.color,
        #                          self.small_area, width = 0)
        
        # This will basically give a rectangle of rectangles
        # We can then delete each smaller rectange as a
        # missile hits it. Not really sure how well it will
        # work though
        
    #def damage(self):
        # a function to calculate damage to block

#class Mystery(object):
    #def __init__(self):

    #Other methods for displaying, updating and images


#class Explosion(object):
    #def __init__(self):

    #Other methods for displaying, updating and images

#class Life(object):
    #def __init__(self):

    #Other methods for displaying, updating and images

class SpaceInvaders(object):
    def __init__(self):
        #Initialize pygame
        pygame.init()

        #Add sounds here

        #Load screen and caption
        #Initialzing a screen for display
        self.screen = pygame.display.set_mode((800,600))
        #Setting Caption of the game
        pygame.display.set_caption('Space Invaders') 

        #Initialzing variables
        self.current_score = 0
        self.lives = 3
        self.current_player = 1
        self.draw_state = 0
        #other variables will also be required

        #Initializing font module
        pygame.font.init()

        #Functions for working on Sound, initial, score, displaying etc.
        #def reset(self):

    def welcome_screen(self):
        self.screen.fill(BLACK)

        self.titleText1 = pygame.font.Font(FONT, 50)
        textsurface = self.titleText1.render('SPACE', False, TITLE_WHITE)
        self.screen.blit(textsurface,(300,120))
        
        self.titleText2 = pygame.font.Font(FONT, 33)
        textsurface = self.titleText2.render('INVADERS', False, LIGHT_GREEN)
        self.screen.blit(textsurface,(300,170))

        #This font will be used for all enemy ships text and Continue text
        self.titleText3 = pygame.font.Font(FONT, 25)

        self.enemy1 = pygame.image.load("./images/enemy3_1.png").convert_alpha()
        self.enemy1 = pygame.transform.scale(self.enemy1 , (40, 40))
        self.screen.blit(self.enemy1, (300, 250))

        textsurface = self.titleText3.render('   =  10 pts', False, GREEN)
        self.screen.blit(textsurface,(350,250))
        
        self.enemy2 = pygame.image.load("./images/enemy2_2.png").convert_alpha()
        self.enemy2 = pygame.transform.scale(self.enemy2 , (40, 40))
        self.screen.blit(self.enemy2, (300, 300))

        textsurface = self.titleText3.render('   =  20 pts', False, BLUE)
        self.screen.blit(textsurface,(350,300))

        self.enemy3 = pygame.image.load("./images/enemy1_2.png").convert_alpha()
        self.enemy3 = pygame.transform.scale(self.enemy3 , (40, 40))
        self.screen.blit(self.enemy3, (300, 350))

        textsurface = self.titleText3.render('   =  30 pts', False, PURPLE)
        self.screen.blit(textsurface,(350,350))

        self.enemy4 = pygame.image.load("./images/mystery.png").convert_alpha()
        self.enemy4 = pygame.transform.scale(self.enemy4 , (80, 40))
        self.screen.blit(self.enemy4, (281, 400))

        textsurface = self.titleText3.render('   =  ?????', False, RED)
        self.screen.blit(textsurface,(350,400))
        
        textsurface = self.titleText3.render('Press any key to continue', False, TITLE_WHITE)
        self.screen.blit(textsurface,(200,500))


    def main(self):
        quit = False
        self.welcome_screen() #Display welcome message
        
        while not quit:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #If user quits game
                    quit = True
            """ if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        #print("Shoot")
                        shoot()
                    if event.key == pygame.K_RIGHT:
                        #print("Right")
                        right()
                    if event.key == pygame.K_LEFT:
                        #print("Left")
                        left()
            if self.draw_state == 0:#If game has just begun
                self.welcome_screen()#Display welcome message

            if self.draw_state > 0: #If game has already begun
                self.screen.fill(BLACK)
                draw()#Draw game matrix

                won = 1
                #If user destroys all enemy ships
                for i in range(0,11):
                    for j in range(0,5):
                        if enemy_ship[i][j]==1: #Checking if any ship is left
                            won = 0

                if won == 1:
                    win_message()#Displaying victory message by calling win_message() function
            """
            pygame.display.update() #Update portions of the screen for software displays

        pygame.quit() #Uninitialize all pygame modules


if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
