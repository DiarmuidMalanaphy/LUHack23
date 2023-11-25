
import pygame
import window
class letter(window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("parchment_alpha.png")

    def display(self,screen):
        self.screen.blit(self.image, (screen.height/4, 0))
        self.screen.blit(text, (SCREEN_WIDTH/4+30,30))
