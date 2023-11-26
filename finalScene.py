import pygame
from window import window


class finalScene(window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("./assets/images/amon.jpg")

    def display(self,screen):
        screen.blit(self.backgroundImg, (screen.get_width()/3 ,screen.get_height()/4))


    def check_event(self,event):
        pass
