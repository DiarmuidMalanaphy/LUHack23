import pygame
import numpy

from door import door
from forensic import forensic
from windowManager import windowManager

class main:
    
    def __init__(self):


        pygame.init()
        SCREEN_WIDTH = 1280
        SCREEN_HEIGHT = 720
        
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        
        pygame.display.set_caption("Hopkins Secret")
        icon_image = pygame.image.load("hopkinsSecret.jpg").convert()
        pygame.display.set_icon(icon_image)
        
        
        clock = pygame.time.Clock()
        
        
        
        running = True
        manager = windowManager(forensic())
        
        while running:
            currentWindow = manager.getCurrentWindow()
            # MAIN GAME LOOP
            #dt = clock.tick(60)
            #dt = dt/40
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #Cursed but might work, will always return None
                new_window = currentWindow.check_event(event)
                manager.changeCurrentWindow(new_window)
                
                    
                                  
                      
            # Get state of all keys
            keys = pygame.key.get_pressed()
            # self.screen.fill((0, 0, 0))
            currentWindow.display(self.screen)
            
            
        

            pygame.display.flip()
            


        # Done! Time to quit.
        pygame.quit()

game = main()