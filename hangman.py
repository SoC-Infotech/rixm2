#Imprt 2 liberie to our game 
import pygame
import random

# Initialize the pygame (game loop, game scene)

pygame.init()
winHeight = 480
winWidth = 700
GREEN = (0,255,0)

#Create window game 
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman by Daniel")

#Main program
# Create a game loop to keep the window visible

inPlay = True
while inPlay:
    win.fill(GREEN) #Make background color green
    pygame.display.update()
    pygame.display.delay(100)
    
#Quit the pygame     
pygame.quit()
