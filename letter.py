
import pygame
import window

class letter(window.window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("parchment_alpha.png")
        self.font = pygame.font.Font("Pixtura12.ttf", 36)
        self.text = "Your text here and also my text over here?"
        self.shiftNumber = 0
        # <- the image is oriented like this.
        self.arrowImage = pygame.image.load('Arrow.png')  # Replace with your image file
        


    def display(self,screen):
        
        screen.blit(self.backgroundImg, (screen.get_height()/4, 0))
        y = 30
        line_spacing = 40
        for text_surface in self.renderText(self.caesarText(self.text,self.shiftNumber)):
            screen.blit(text_surface, (screen.get_width()/4, y))
            y += line_spacing  # Move y to the next line

        self.backArrowButton = self.arrowImage.get_rect(center=(screen.get_height()/3*2, screen.get_height() / 2))
        screen.blit(self.arrowImage, self.backArrowButton.topleft)
    
    def check_button_click(self, mouse_pos):
        if self.backArrowButton.collidepoint(mouse_pos):
            # Perform an action when the button is clicked
            print("Back arrow clicked!")
        
        
        

    def renderText(self,text):  
        words = text.split()
        chunk_size = 6
        chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
        rendered_texts = [self.font.render(chunk, True, (255, 0, 0)) for chunk in chunks]
        return rendered_texts
    


    
    def caesarText(self, text, shiftNumber):
        # Define the transformation for each character
        def shift_char(c):
            if c.isalpha():
                start = ord('a') if c.islower() else ord('A')
                return chr((ord(c) - start + shiftNumber) % 26 + start)
            return c

        # Apply the transformation to each character in the text
        return ''.join(shift_char(c) for c in text)
