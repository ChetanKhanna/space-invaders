#Importing required modules
import pygame
import random

#Initializing pygame modules
pygame.init()

#Initializing font module
pygame.font.init()

#Creating fonts
#add game fonts here

#Defining RGB values for colours        #If it's okay, let's just keep the game Black and White
BLACK = ( 0, 0, 0)                      #Gives the game an arcade touch I believe :)
WHITE = (255, 255, 255)

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

## shots to kill defender in easy level, 2 for medium and 1 for high diffiulty level
DIFFICULTY = {"HIGH":1, "MEDIUM":2, "LOW":3}
#Defining window boundaries and game boundaries
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
GAME_WIDTH = WINDOW_WIDTH - 100         #Ships will move in this area
GAME_HEIGHT = WINDOW_HEIGHT - 250
STONE_HEIGHT                            #Once the ships reach this depth, Game Over[Co-ordinates to be decided]

SHIP_VERTICAL_VELOCITY                  #Velocity to be decided
SHIP_HORIZONTAL_VELOCITY
DEFENDER_VERTICAL_VELOCITY
#The idea is that different rows of ship can fire at different rates, say the tougher ones fire more rapidly
SHIP_FIRE_RATE
DEFENDER_FIRE_RATE 

SHIP_MISSILE_SIZE                 #missile size to be decided
DEFENDER_MISSILE_SIZE


screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #Initialzing a screen for display
pygame.display.set_caption('Space Invaders')

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

#Classes for all game parts like ship, enemy_ship, laser etc.
#To draw the game matrix, scores and buttons
def draw():
    #TODO add everything related to game
    global ships

#To shoot from the ship
def shoot():
    global ships

#To go Right
def right():
    global ships

#To go Left
def left():
    print("left")
    global ships

def welcome_message():
    global current_player
    # Welcome screen

def win_message():
    global score_player1, score_player2

def main():
    welcome_message() #Display welcome message
    quit = False

    while not quit:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:#If user quits game
                quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #print("Shoot")
                    shoot()
                if event.key == pygame.K_RIGHT:
                    #print("Right")
                    right()
                if event.key == pygame.K_LEFT:
                    #print("Left")
                    left()
        if draw_state == 0:#If game has just begun
            welcome_message()#Display welcome message

        if draw_state > 0:#If game has already begun
            draw()#Draw game matrix

            won = 1
            #If user destroys all enemy ships
            for i in range(0,11):
                for j in range(0,5):
                    if enemy_ship[i][j]==1: #Checking if any ship is left
                        won = 0

            if won == 1:
                win_message()#Displaying victory message by calling win_message() function

        pygame.display.update() #Update portions of the screen for software displays

    pygame.quit() #Uninitialize all pygame modules


main()
