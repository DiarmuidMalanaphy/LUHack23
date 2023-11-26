import pygame
import numpy
from Console import Console

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
        manager = windowManager(door())
        self.font = pygame.font.Font(None, 60)
        clock_started = False
        time_remaining = 20*60
        while running:
            currentWindow = manager.getCurrentWindow()
            # MAIN GAME LOOP
            dt = clock.tick(60)
            #dt = dt/40
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                #Cursed but might work, will always return None
                new_window = currentWindow.check_event(event)
                
                if new_window is not None and not clock_started:
                    if new_window[1] is None:
                        clock_started = True
                    
                
                manager.changeCurrentWindow(new_window)
            if clock_started:
                    time_remaining -= dt / 1000.0
                
                    
                                  
                      
            # Get state of all keys
            keys = pygame.key.get_pressed()
            # self.screen.fill((0, 0, 0))
            currentWindow.display(self.screen)
            
            if clock_started:
                mins, secs = divmod(int(time_remaining), 60)
                timer_text = '{:02d}:{:02d}'.format(mins, secs)
                text_surface = self.font.render(timer_text, True, (255, 255, 255))

                # Create a new surface for the timer with transparency
                timer_surface = pygame.Surface((text_surface.get_width(), text_surface.get_height()))
                timer_surface.set_alpha(128)  # Adjust alpha for transparency (0-255)
                timer_surface.fill((0, 0, 0))  # Fill with a background color if needed

                # Blit the timer text onto the timer surface
                x_position = SCREEN_WIDTH / 2 - timer_surface.get_width() / 2
                y_position = 50  # Gap from the top
                timer_surface.blit(text_surface, (0, 0))
                self.screen.blit(timer_surface, (x_position, y_position))
            

            # Blit the timer surface onto the main screen
            

            pygame.display.flip()
            


        # Done! Time to quit.
        pygame.quit()

game = main()