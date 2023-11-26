import pygame
import window

class Padlock(window.window):

    def __init__(self):
        pass

    def display(self, screen):
        # self.button = pygame.Rect(100, 100, 25, 25)
        self.button = pygame.font.Font(None, 32).render("1", True, (255,255,255)).get_rect(center=(100,100))
        pygame.draw.rect(screen, (0, 255, 255), self.button)
        # screen.blit(self.button, (100, 100))
        pass

    def check_event(self, event):
        pass
