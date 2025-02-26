import pygame
import random
import os
import time
import math
# Initialize Pygame
pygame.init()

# Set up the display
win = pygame.display.set_mode((500, 500))  
pygame.display.set_caption("My First Game")
win.fill((255,255, 255)) # for a white background

# to set the font
font = pygame.font.SysFont('arial',24)
draw=True
tdistance = 0 # to calculate the total disrance
run=True # runs the main loop
radius=10
pos=(0,0)
points=[] # stores the points of the created circles

# To calculate the distance between the points
def calculatedist(p1,p2):
    return math.sqrt((p2[0] -p1[0])**2 + (p2[1] -p1[1])**2)

def draw():
     win.fill((255,255,255))
     #Draw the lines connecting the points
     if len(points) > 1 :
        for i in range(len(points) - 1):
            pygame.draw.line(win,(0,0,0),points[i],points[i+1],2)
                
     for point in points:
        colour =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        pygame.draw.circle(win, colour, point, radius)
        # Display the total distance
     if points:
        path_text = f"Total Path Length: {tdistance:.2f} pixels"
        text = font.render(path_text,True,(0,0,0))
        win.blit(text, (10, 10))
    # Update the display after each draiwng
     pygame.display.update()
    
       

    
             
while run:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT :
            run=False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Click event 
            if event.button == 1:
                mouse_pos=event.pos
                points.append(mouse_pos)
                 # calculate the total points

                if len(points) >1:
                    distance = calculatedist(points[-2],points[-1])
                    tdistance += distance
                    print(f"Added point {len(points)}.Distance from previous point : {distance : 2f}")

            elif event.button == 3 and points : # right click to delete the last circle
                if len(points) > 1:
                    tdistance -= calculatedist(points[-2],points[-1])
                points.pop()
            
        elif event.type == pygame.KEYDOWN : # click spacebar to clear the creen
            if event.key == pygame.K_SPACE:
                points =[]
                tdistance = 0

            elif event.key == pygame.K_s : # click the s button to save
                pygame.image.save(win,"drawing.png")
            
    draw() # redraw and update the creen

        
    
    
pygame.quit()