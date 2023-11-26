
import time
import pygame
import window

class letter(window.window):
    def __init__(self):
        self.backgroundImg = pygame.image.load("parchment_alpha.png")
        self.font = pygame.font.Font("Pixtura12.ttf", 32)
        self.text = "Julius Caesar used to encrypt his messages using this cipher, all the letters are shifted by a certain number, a becomes z, b becomes a. That being said, this puzzle is your introduction. He is coming. The code to the monitor is thirty-nine thousand?"
        self.shiftNumber = 3
        # <- the image is oriented like this.
        self.arrowImage = pygame.image.load('Arrow.png')  # Replace with your image file
        self.input_text = ""
        self.dialImg = pygame.image.load("dial.png")
        self.dialDrag = False
    

        


    def display(self,screen):
        # Dial
        self.dialButton = self.dialImg.get_rect(center=(screen.get_width()*3 / 4, screen.get_height()*2 /4 ))
        screen.blit(self.dialImg, self.dialButton)
        
        screen.blit(self.backgroundImg, (screen.get_height()*3/8, 110))
        y = 190
        line_spacing = 40
        for text_surface in self.renderText(self.caesarText(self.text,self.shiftNumber)):
            screen.blit(text_surface, (screen.get_width()/4, y))
            y += line_spacing  # Move y to the next line

        

        self.backArrowButton = self.arrowImage.get_rect(center=(screen.get_width() / 4, screen.get_height() * 2 / 4 + 200 ))
        screen.blit(self.arrowImage, self.backArrowButton.topleft)
    
    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if self.backArrowButton.collidepoint(event.pos):
                # Perform an action when the button is clicked
                pygame.mixer.init()
                scaryVoice = pygame.mixer.Sound("warning.mp3")#
                sound = pygame.mixer.Sound("scarynoise.mp3")
                sound.set_volume(0.4)
                scaryVoice.play()

            
                
                sound.play()
                time.sleep(1)
                sound.set_volume(0.6)
                time.sleep(1)
                sound.set_volume(0.8)
                time.sleep(1)

                # Restore the volume if needed
                sound.set_volume(1.0)
                return((True,None))
            if self.input_text == '':
                    self.input_text = '0'
            self.input_text = str (int(self.input_text) + 1)
            self.shiftNumber = int(self.input_text)
            
            if self.dialButton.collidepoint(event.pos):
                self.dialDrag = True
                self.mouseX, self.mouseY = event.pos
                self.offsetX = self.dialButton.x - self.mouseX
                self.offsetY = self.dialButton.y - self.mouseY
                # self.shiftNumber += 1
                # self.caesarText(self.text, self.shiftNumber)
            
                
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dialDrag = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dialDrag:
                self.mouseX, self.mouseY = event.pos
                offsetX = self.dialButton.x - self.mouseX
                offsetY = self.dialButton.y - self.mouseY

                # self.offsetX = self.dialButton.x - self.mouseX
                # self.offsetY = self.dialButton.y - self.mouseY
                print("X: " + str(self.offsetX) + "   Y:" + str(self.offsetY))
                print("X: " + str(offsetX) + "   Y:" + str(offsetY))
                if (offsetX + offsetY) - (self.offsetX + self.offsetY) > 0:
                    self.shiftNumber += 1
                else:
                    self.shiftNumber -= 1
                self.offsetX = offsetX
                self.offsetY = offsetY
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # When Enter is pressed, set the Caesar shift number
                if self.input_text.isdigit():
                    self.shiftNumber = int(self.input_text)
                    print("Shift number set to:", self.shiftNumber)
                self.input_text = ''  # Optionally clear the input box
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.unicode.isdigit():
                # Append the input if it's a digit
                self.input_text += event.unicode
            elif event.key == pygame.K_UP:
                if self.input_text == '':
                    self.input_text = '0'
                self.input_text = str (int(self.input_text) + 1)
                self.shiftNumber = int(self.input_text)
            elif event.key == pygame.K_DOWN:
                if self.input_text == '':
                    self.input_text = '0'
                if int(self.input_text)>0:
                    self.input_text = str(int(self.input_text)-1)
                    self.shiftNumber = int(self.input_text)
                else:
                    self.input_text = '25'
                    self.shiftNumber = 25
        
        
        
        

    def renderText(self,text):  
        words = text.split()
        chunk_size = 5
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
