#Importing required modules
import pygame
import random

#Defining RGB values for colours
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800,600)) #Initialzing a screen for display
# adding font file
FONT = "fonts/space_invaders.ttf"
pygame.display.set_caption('Space Invaders')


#List to store enemy ships
ships = [
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1]
]

#Initialzing variables
score_player1 = 0
score_player2 = 0
lives = 3
current_player = 1
draw_state = 0
#other variables will also be required

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
        
    def shoot(self)
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
            
    def move_down(self, movement):
        # to make the ship come down
        
    def move_horizontal(self, movement): 
        # to make ship oscilate horizontally
        
    def shoot(self):
        # not all ships will shoot at once, we need to randomly select some of them
        # and call the Missile.shoot function or something to make them shoot


class Blocker(pygame.sprite.Sprite):
    """
    Class for defining blocks and their properties;
    basically their damage rate.
    """
    def __init__(self, block_image):
        super.()__init__()
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
        
    def damage(self):
        # a function to calculate damage to block

class Mystery(object):
	def __init__(self):

	#Other methods for displaying, updating and images


class Explosion(object):
	def __init__(self):

    #Other methods for displaying, updating and images

class Life(object):
	def __init__(self):

	#Other methods for displaying, updating and images

class Text(object):
	def __init__(self):

    #Other methods for displaying, updating and images


class SpaceInvaders(object):
	def __init__(self):

	def reset(self):

	#Functions for working on Sound, initial, score, displaying etc.

	def main(self):


if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
