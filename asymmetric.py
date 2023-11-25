import pygame
import window
class asymmetric(window):
    def __init__(self, screen):
        self.backgroundImg = screen.fill("gray")

    def display(self,screen):
        self.screen.blit(self.image, (screen.height/4, 0))
        self.screen.blit(text, (SCREEN_WIDTH/4+30,30))