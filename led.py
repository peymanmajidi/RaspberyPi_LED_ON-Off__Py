import RPi.GPIO as IO            # calling header file for GPIO’s of PI
import time
import pygame


IO.setwarnings(False)
IO.setmode (IO.BOARD)       # programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
IO.setup(40,IO.OUT)         # initialize digital pin40 as an output.


# Initiate pygame
pygame.init()

# Game window


WIDTH = 460
HEIGHT = 300

COLOR = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
clicked = False

# Game title
pygame.display.set_caption("RSA | LED Controler")
# pygame.draw.rect(window, COLOR, [ x ,HEIGHT  , CHARCTER , CHARCTER ], 0 )
pygame.display.update()
game_over = False

flashing= False

while not game_over:
        time.sleep(0.05)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = not clicked

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_UP:
                        game_over= True
        if clicked:
                pygame.draw.rect(window, RED, [0,0,WIDTH,HEIGHT],0)
                pygame.display.update()
                if flashing:
                        IO.output(40,1)
                        flashing = False
                else:
                        IO.output(40,0)
                        flashing = True

                                         
                
            
        if not clicked:
                pygame.draw.rect(window, BLACK, [0,0,WIDTH,HEIGHT],0)
                IO.output(40,0)
                pygame.display.update()





        
