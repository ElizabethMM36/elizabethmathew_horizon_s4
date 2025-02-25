import pygame
import random
import time
# Initialize Pygame
pygame.init()

# Set up the display
win = pygame.display.set_mode((500, 500))  
pygame.display.set_caption("My First Game")
win.fill((255,255, 255)) # for a white background

width=40

draw=True
stime= 0 #initilizing start time
run=True
while run:
    
    pygame.time.delay(100)
    for event in pygame.event.get():
        radius=10
        if event.type == pygame.QUIT :
            run=False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Click event 
            if event.button == 1:
                draw=True 
                stime= time.time()
                mouse_pos=event.pos
                print("Left  mouse button pressed") 
        elif event.type == pygame.MOUSEBUTTONUP:  # Mouse released 
            if event.button == 1 and draw == True:
                draw=False
                randomcolour= ( random.randint(0,255),random.randint(0,255),random.randint(0,255))
                increment=time.time()-stime
                radius+=int(50*increment)
                pygame.draw.circle(win,randomcolour,mouse_pos,radius)
             
        pygame.display.update()
    
    
    
pygame.quit()
import pygame
import random
import time
# Initialize Pygame
pygame.init()

# Set up the display
win = pygame.display.set_mode((500, 500))  
pygame.display.set_caption("My First Game")
win.fill((255,255, 255)) # for a white background

width=40

draw=True
stime= 0 #initilizing start time
run=True
while run:

    pygame.time.delay(100)
    for event in pygame.event.get():
        radius=10
        if event.type == pygame.QUIT :
            run=False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Click event 
            if event.button == 1:
                draw=True 
                stime= time.time()
                mouse_pos=event.pos
                print("Left  mouse button pressed") 
        elif event.type == pygame.MOUSEBUTTONUP:  # Mouse released 
            if event.button == 1 and draw == True:
                draw=False
                randomcolour= ( random.randint(0,255),random.randint(0,255),random.randint(0,255))
                increment=time.time()-stime
                radius+=int(50*increment)
                pygame.draw.circle(win,randomcolour,mouse_pos,radius)

        pygame.display.update()



pygame.quit()
