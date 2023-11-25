import pygame
import window
class forensic(window.window):
    def __init__(self, screen):
        self.backgroundImg = pygame.image.load("translatepic.png").convert()
        self.font = pygame.font.Font("Pixtura12.ttf", 36)
        self.text = "Forensic ling puzzle text here"
        self.arrowImage = pygame.image.load("Arrow.png").convert()
        self.input_text = ""
        self.guess = ""
        self.solution = "192.88.247.82"

    def display(self,screen):
        
        screen.blit(self.backgroundImg, (screen.get_height()/4, 0))
        y = 30
        line_spacing = 40
        for text_surface in self.renderText(self.text):
            screen.blit(text_surface, (screen.get_width()/4, y))
            y += line_spacing  # Move y to the next line
        
        self.backArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 5, screen.get_height() * 3 / 4 + 20))
        screen.blit(self.arrowImage, self.backArrowButton.topleft)

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.backArrowButton.collidepoint(event.pos):
                # Perform an action when the button is clicked
                print("Back arrow clicked!")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # When Enter is pressed, set the guess
                if self.input_text is not "":
                    self.guess = str(self.input_text)
                else:
                    self.guess = "empty."
                print("Your guess is", self.guess)
                if self.guess is self.solution:
                    print("You are correct!")
                else:
                    print("Incorrect.")
                self.input_text = ''  # Optionally clear the input box
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.unicode.isdigit() or event.unicode.equals("."):
                # Append the input
                self.input_text += event.unicode
            
            


    def renderText(self,text):
        
        words = text.split()
        chunk_size = 6
        chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

        rendered_texts = [self.font.render(chunk, True, (255, 0, 0)) for chunk in chunks]

        return rendered_texts