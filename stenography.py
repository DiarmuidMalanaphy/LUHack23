import pygame
import window
class stenography(window.window):
    def __init__(self, screen):
        self.backgroundImg = screen.fill("gray")
        self.font = pygame.font.Font("Pixtura12.ttf", 36)
        self.text = "Stenography puzzle text here"


    def display(self,screen):
        
        screen.blit(self.backgroundImg, (screen.get_height()/4, 0))
        y = 30
        line_spacing = 40
        for text_surface in self.renderText(self.text):
            screen.blit(text_surface, (screen.get_width()/4, y))
            y += line_spacing  # Move y to the next line
        

    def renderText(self,text):
        
        words = text.split()
        chunk_size = 6
        chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

        rendered_texts = [self.font.render(chunk, True, (255, 0, 0)) for chunk in chunks]

        return rendered_texts