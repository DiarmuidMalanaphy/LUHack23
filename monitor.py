import pygame
import door
from vent import vent
import window


class monitor(window.window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("monitor.png")
        self.arrowImage = pygame.image.load('Arrow.png')

    def display(self, screen):
        screen.blit(self.backgroundImg, (0, 0))

        # Left Arrow Button
        self.leftArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 4, screen.get_height() *3/ 4))
        screen.blit(self.arrowImage, self.leftArrowButton.topleft)

        # Right Arrow Button (flipped)
        flipped_arrow_image = pygame.transform.flip(self.arrowImage, True, False)  # Flip the image
        self.rightArrowButton = flipped_arrow_image.get_rect(center=(screen.get_width() * 3 / 4, screen.get_height() *3/ 4))
        screen.blit(flipped_arrow_image, self.rightArrowButton.topleft)


    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            
            if self.leftArrowButton.collidepoint(event.pos):
                return(False,door.door())
            if self.rightArrowButton.collidepoint(event.pos):
                return(False,vent())
                    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pass
                # return((False,letter()))
        
        
        
            
        
        
                