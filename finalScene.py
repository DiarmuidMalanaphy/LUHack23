import pygame
from window import window


class finalScene(window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("5Unsettling.JPEG")

    def display(self,screen):
        screen.blit(self.backgroundImg, (0, 0))


    def check_event(self,event):
        pass
