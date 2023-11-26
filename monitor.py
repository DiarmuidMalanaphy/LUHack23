import os
import pygame
from Console import Console
import door
from vent import vent
import window


class monitor(window.window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("./assets/images/monitor.png")
        self.arrowImage = pygame.image.load('./assets/images/Arrow.png')
        try:
            pygame.mixer.init()
            doorOpening = pygame.mixer.Sound("./assets/audio/doorOpening.mp3")
            os.rename('./assets/audio/doorOpening.mp3', './assets/audio/doorOpening1.mp3')
            doorOpening.play()
        except Exception:
            pygame.mixer.init()
            doorOpening = pygame.mixer.Sound("./assets/audio/behindYou.mp3")
            doorOpening.play()
            pass


    def display(self, screen):
        screen.blit(self.backgroundImg, (0, 0))

        # Left Arrow Button
        self.leftArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 8, screen.get_height() *2 / 4 +10))
        screen.blit(self.arrowImage, self.leftArrowButton.topleft)

        # Right Arrow Button (flipped)
        flipped_arrow_image = pygame.transform.flip(self.arrowImage, True, False)  # Flip the image
        self.rightArrowButton = flipped_arrow_image.get_rect(center=(screen.get_width() * 7 / 8, screen.get_height() *2 / 4 +10))
        screen.blit(flipped_arrow_image, self.rightArrowButton.topleft)


    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            
            if self.leftArrowButton.collidepoint(event.pos):
                return(False,door.door())
            if self.rightArrowButton.collidepoint(event.pos):
                return(False,vent())
            

            monitor = pygame.Rect(171,242, 426, 362)
            if monitor.collidepoint(event.pos):

                return(False,Console())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pass
                # return((False,letter()))
