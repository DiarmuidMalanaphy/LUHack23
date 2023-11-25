import pygame
import window
class phishing(window.window):
    def __init__(self, screen):
        self.backgroundImg = screen.fill("gray")
        self.font = pygame.font.Font("Pixtura12.ttf", 36)
        self.text = "Phishing puzzle text here"


    def display(self,screen):
        
        screen.blit(self.backgroundImg, (screen.get_height()/4, 0))
        y = 30
        line_spacing = 40
        for text_surface in self.renderText(self.text):
            screen.blit(text_surface, (screen.get_width()/4, y))
            y += line_spacing  # Move y to the next line
        

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if self.backArrowButton.collidepoint(event.pos):
                # Perform an action when the button is clicked
                print("Back arrow clicked!")