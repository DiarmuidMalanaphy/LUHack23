import pygame
import window
from finalScene import finalScene

class Padlock(window.window):

    def __init__(self):
        self.keypadImage = pygame.image.load('keypad.jpg')
        self.code = ""
        self.numClicked = 0

    def display(self, screen):
        # self.button = pygame.Rect(100, 100, 25, 25)
        
        self.keypad = self.keypadImage.get_rect(center=(screen.get_width() / 2, screen.get_height()  / 2 ))
        screen.blit(self.keypadImage, self.keypad.topleft)

        # pygame.draw.circle(screen, (255,255,255), (500, 170), 30)
        # pygame.draw.circle(screen, (255,255,255), (580, 170), 30)
        # pygame.draw.circle(screen, (255,255,255), (660, 170), 30)
        # pygame.draw.circle(screen, (255,255,255), (740, 170), 30)

        
        # screen.blit(self.button, (100, 100))

    #def updatePinTrack(self):
        colors = [(255,255,255)]*4
        for i in range(self.numClicked):
            colors[i] = (0,0,255)
        for i in range(4):
            pygame.draw.circle(screen, colors[i], (500+80*i, 170), 30)

    def check_event(self, event):
        #I'm going fucking crazy
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            one   = pygame.Rect(500, 230, 75, 60)
            two   = pygame.Rect(585, 230, 75, 60)
            three = pygame.Rect(670, 230, 75, 60)
            four  = pygame.Rect(500, 300, 75, 60)
            five  = pygame.Rect(585, 300, 75, 60)
            six   = pygame.Rect(670, 300, 75, 60)
            seven = pygame.Rect(500, 370, 75, 60)
            eight = pygame.Rect(585, 370, 75, 60)
            nine  = pygame.Rect(670, 370, 75, 60)
            zero  = pygame.Rect(585, 440, 75, 60)
            hash  = pygame.Rect(670, 440, 75, 60)
            #pygame.draw.rect(screen, (255,0,0), one)



            if one.collidepoint(event.pos):
                self.code += "1"
                self.numClicked += 1
            elif two.collidepoint(event.pos):
                self.code += "2"
                self.numClicked += 1
            
            elif three.collidepoint(event.pos):
                self.code += "3"
                self.numClicked += 1
            
            elif four.collidepoint(event.pos):
                self.code += "4"
                self.numClicked += 1
            
            elif five.collidepoint(event.pos):
                self.code += "5"
                self.numClicked += 1
            
            elif six.collidepoint(event.pos):
                self.code += "6"
                self.numClicked += 1
            
            elif seven.collidepoint(event.pos):
                self.code += "7"
                self.numClicked += 1
            
            elif eight.collidepoint(event.pos):
                self.code += "8"
                self.numClicked += 1
            
            elif nine.collidepoint(event.pos):
                self.code += "9"
                self.numClicked += 1
            elif zero.collidepoint(event.pos):
                self.code += "0"
                self.numClicked += 1
            ##I understand this is horrible practice but i can't think straight right now i should be multiplying and for looping this.
           
            elif hash.collidepoint(event.pos):
                self.code = []
                self.numClicked = 0
            
            if self.numClicked == 4:
                if self.code == "2000":
                    return((False, finalScene()))
                else:
                    self.code = ""
                    self.numClicked = 0;

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return((True, None))

