import pygame
import numpy


class main:
    
    def __init__(self):


        pygame.init()
        SCREEN_WIDTH = 1024
        SCREEN_HEIGHT = 524
        
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        
        pygame.display.set_caption("Hopkins Secret")
        icon_image = pygame.image.load("hopkinsSecret.jpg")
        pygame.display.set_icon(icon_image)
        #self.image = pygame.image.load("hopkinsSecret.jpg")
        
        
        clock = pygame.time.Clock()
        
        
        
        running = True
        while running:
            # MAIN GAME LOOP
            dt = clock.tick(60)
            dt = dt/40
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                    
                                  
                      
            # Get state of all keys
            keys = pygame.key.get_pressed()
            self.screen.fill((0, 0, 0))
            
            #self.screen.blit(self.image, (0, 0))
        

            pygame.display.flip()
            


        # Done! Time to quit.
        pygame.quit()

game = main()