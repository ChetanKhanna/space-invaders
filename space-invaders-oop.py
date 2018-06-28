#Importing required modules
import pygame
import random

#Defining RGB values for colours
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((800,600)) #Initialzing a screen for display
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

class Defender(pygame.sprite.Sprite):   #Ship was confusing me with the ships [] above
    """                                 
    Defining the defender spaceship and its
    properties
    """
    def __init__(self,defender_image, x_pos, y_pos):
        super().__init__()
        
        self.image = pygame.image.load("defender.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = (x_pos, y_pos))
        pass
        
    def left(self, movement):
        self.rect.x += movement # we will need a limit; if rect.x goes beyond that limit, 
                                # it will hit the wall or something and hence, won't increase
        pass
        
    def right(self, movement):
        self.rect.x -= movement
        pass
        
    def shoot(self):
       # Missile.shoot() # missile is another class
                        # not sure, still
       pass
  
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
        pass
        
    def shoot(self):
        # if it goes beyond certain dimension, self.kill()
        # self.rect.y += self.speed * self.direction
        pass


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
        pass 
            
    def move_down(self, movement):
        # to make the ship come down
        pass
        
    def move_horizontal(self, movement): 
        # to make ship oscilate horizontally
        pass
        
    def shoot(self):
        # not all ships will shoot at once, we need to randomly select some of them
        # and call the Missile.shoot function or something to make them shoot
        pass

class Blocker(pygame.sprite.Sprite):
    """
    Class for defining blocks and their properties;
    basically their damage rate.
    """
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        
    def draw(self):
        # pygame.draw.rect(screen, WHITE, [self.x, self.y, 125,  60])
        
        # instead of making it single rectangle, distributed each 
        # rectangle into 25 smaller rectangles. Thought this may
        # help in collision detection and we can delete smaller rectangles 
        # when a missile hits it.
        for i in range(5):
            for j in range(5):
                x_pos = self.x + 25*j
                y_pos = self.y + 12*i
                pygame.draw.rect(screen, WHITE, [x_pos, y_pos, 25, 12])
        
    def damage(self):
        # a function to calculate damage to block
        pass
        

class Mystery(object):
    def __init__(self):

    #Other methods for displaying, updating and images
        pass
    
class Explosion(object):
    def __init__(self):

    #Other methods for displaying, updating and images
        pass
    
class Life(object):
    def __init__(self):

	#Other methods for displaying, updating and images
        pass
    
class Text(object):
    def __init__(self):

    #Other methods for displaying, updating and images
        pass

class SpaceInvaders(object):
    def __init__(self):
        pass

    def reset(self):
        pass

	#Functions for working on Sound, initial, score, displaying etc.

    def main(self):
        block_1 = Blocker(75,450)
        block_2 = Blocker(337.5,450)
        block_3 = Blocker(600, 450)
        block_1.draw()
        block_2.draw()
        block_3.draw()
        pygame.display.update()

if __name__ == '__main__':
    game = SpaceInvaders()
    game.main()
