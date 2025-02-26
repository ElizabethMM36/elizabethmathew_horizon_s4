import pygame
import random
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
run=True
radius=10
pos=(0,0)
points=[] 
def calculatedist(p1,p2):
    return math.sqrt((p2[0] -p1[0])**2 + (p2[1] -p1[1])**2)
while run:
    
    pygame.time.delay(100)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT :
            run=False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Click event 
            if event.button == 1:
                mouse_pos=event.pos
                points.append(mouse_pos)
                

                if len(points) >1:
                    distance = calculatedist(points[-2],points[-1])
                    tdistance += distance
                    print(f"Added point {len(points)}.Distance from previous point : {distance : 2f}")
                

                # To draw the lines
                win.fill((255,255,255))


                # Draw the lines connecting points
                if len(points) > 1 :
                    for i in range(len(points) - 1):
                        pygame.draw.line(win,(0,0,0),points[i],points[i+1],2)
                
                for point in points:
                    colour =(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                    pygame.draw.circle(win, colour, point, radius)

                if len(points) > 1:
                    path_text = f"Total Path Length: {tdistance:.2f} pixels"
                    text = font.render(path_text,True,(0,0,0))
                    win.blit(text, (10, 10))
        pygame.display.update()
    
    
    
pygame.quit()
