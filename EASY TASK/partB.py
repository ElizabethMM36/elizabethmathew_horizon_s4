import pygame
import random
import time
# Initialize Pygame
pygame.init()

# Set up the display
win = pygame.display.set_mode((500, 500))  
pygame.display.set_caption("My First Game")
win.fill((255,255, 255)) # for a white background
width = 30
draw=True
stime= 0 #initilizing start time
run=True
radius=10
