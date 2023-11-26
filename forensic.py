import pygame
import window
class forensic(window.window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("translatepic.png")
        # self.font = pygame.font.Font("Pixtura12.ttf", 36)
        self.text = "Forensic ling puzzle text here"
        self.arrowImage = pygame.image.load("Arrow.png")
        self.input_text = ""
        self.guess = ""
        self.solution = "192.88.247.82"
        self.textbox = pygame.Surface((100,100))
        # self.textbox = pygame.Rect(100,100,140,32)
        self.textboxActive = False

    def display(self,screen):
        self.backgroundImg = pygame.transform.scale(self.backgroundImg, (700,700))
        screen.blit(self.backgroundImg, (screen.get_height()/4, 0))
        y = 30
        line_spacing = 40
        # for text_surface in self.renderText(self.text):
        #     screen.blit(text_surface, (screen.get_width()/4, y))
        #     y += line_spacing  # Move y to the next line        
        self.backArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 5, screen.get_height() * 3 / 4 + 20))
        screen.blit(self.arrowImage, self.backArrowButton.topleft)
        # self.textboxi = self.textbox.get_rect(center=(screen.get_width()/5, screen.get_height() * 3 / 4 + 20))
        # screen.blit(self.textbox, (650,650))

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.backArrowButton.collidepoint(event.pos):
                # Perform an action when the button is clicked
                print("Back arrow clicked!")
            #     self.textboxActive = False
            # elif self.textbox.collidepoint(event.pos):
            #     self.textboxActive = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # When Enter is pressed, set the guess
                if self.input_text != "":
                    self.guess = str(self.input_text)
                else:
                    self.guess = "empty."
                print("Your guess is", self.guess)
                if self.guess == self.solution:
                    print("You are correct!")
                else:
                    print("Incorrect.")
                self.input_text = ''  # Optionally clear the input box
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.unicode.isdigit() or event.unicode == ".":
                # Append the input
                self.input_text += event.unicode
            



    # def renderText(self,text):
        
    #     words = text.split()
    #     chunk_size = 6
    #     chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

    #     rendered_texts = [self.font.render(chunk, True, (255, 0, 0)) for chunk in chunks]

    #     return rendered_texts
    
forensic()
