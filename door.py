import pygame
from letter import letter
import window

class door(window.window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("door.png")
        self.arrowImage = pygame.image.load('Arrow.png')

    def display(self, screen):
        screen.blit(self.backgroundImg, (0, 0))
        self.leftArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 4, screen.get_height() * 2 / 4 ))
        screen.blit(self.arrowImage, self.leftArrowButton.topleft)

        self.rightArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 4, screen.get_height() * 2 / 4 ))
        rightArrow = pygame.transform.flip(self.arrowImage, True, False)
        screen.blit(rightArrow, self.leftArrowButton.topleft)


    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            
            if self.leftArrowButton.collidepoint(event.pos):
                return(False,)
                    
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return((False,letter()))
        
            if self.backArrowButton.collidepoint(event.pos):
                # Perform an action when the button is clicked
                return((True,None))
        
        
                