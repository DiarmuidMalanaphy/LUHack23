import pygame 
import door
from forensic import forensic



import monitor

import window
class vent(window.window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("./assets/images/vent.png")
        self.arrowImage = pygame.image.load('./assets/images/Arrow.png')

    def display(self, screen):
        screen.blit(self.backgroundImg, (0, 0))

        # Left Arrow Button
        self.leftArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 8, screen.get_height() *2 / 4 +10))
        screen.blit(self.arrowImage, self.leftArrowButton.topleft)

        # Right Arrow Button (flipped)
        flipped_arrow_image = pygame.transform.flip(self.arrowImage, True, False)  # Flip the image
        self.rightArrowButton = flipped_arrow_image.get_rect(center=(screen.get_width() * 7 / 8, screen.get_height() *2 / 4 +10))
        screen.blit(flipped_arrow_image, self.rightArrowButton.topleft)


        riddleProposition = pygame.image.load("./assets/images/riddleProposition.png")  # Replace with the actual file path


        # Get the rect of the image and set its center to the middle of the screen
        self.riddlePropositionRect = riddleProposition.get_rect(center=(screen.get_width()*3 / 8, screen.get_height()* 3 / 10))

        # Blit the image at the rect's top-left coordinate
        screen.blit(riddleProposition, self.riddlePropositionRect.topleft)

        
        self.backgroundImg = pygame.image.load("./assets/images/vent.png")


    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            
            if self.leftArrowButton.collidepoint(event.pos):
                return(False,monitor.monitor())
            if self.rightArrowButton.collidepoint(event.pos):
                return(False,door.door())
            
            if self.riddlePropositionRect.collidepoint(event.pos):
                return(False,forensic())
            
            vent = pygame.Rect(143, 358, 900, 302)
            if vent.collidepoint(event.pos):
                self.backgroundImg = pygame.image.load("./assets/images/ventmon.png")

    
            print(event.pos)
            
                    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pass
                # return((False,amongus()))
        
            



        
