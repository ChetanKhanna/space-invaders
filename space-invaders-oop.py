#Importing required modules
import pygame
import random

#Defining RGB values for colours
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((600,800)) #Initialzing a screen for display
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

class Ship(object):
    def __init__(self):

    def update(self):

class Bullet(object):
	def __init__(self):

	def update(self):


class Enemy(object):
	def __init__(self, row, column):

	#Other methods for displaying, updating and images


class Blocker(object):
	def __init__(self):

    #Other methods for displaying, updating and images

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

game = SpaceInvaders()
game.main()
