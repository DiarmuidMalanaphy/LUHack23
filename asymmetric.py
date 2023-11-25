import pygame
import window
class asymmetric(window.window):
    def __init__(self, screen):
        self.backgroundImg = screen.fill("gray")
        self.font = pygame.font.Font("Pixtura12.ttf", 36)
        self.text = "Asymmetric puzzle text here"

    def display(self,screen):
        screen.blit(self.backgroundImg, (screen.get_height()/4, 0))
        screen.blit(self.text, (screen.get_width()/4+30,30))