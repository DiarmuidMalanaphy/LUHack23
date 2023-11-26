import pygame
import window

class Padlock(window.window):

    def __init__(self):
        self.keypadImage = pygame.image.load('keypad.jpg')
        
        self.code = []
        pass

    def display(self, screen):
        # self.button = pygame.Rect(100, 100, 25, 25)
        
        self.keypad = self.keypadImage.get_rect(center=(screen.get_width() / 2, screen.get_height()  / 2 ))
        screen.blit(self.keypadImage, self.keypad.topleft)


        
        # screen.blit(self.button, (100, 100))
        pass

    def check_event(self, event):
        #I'm going fucking crazy
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos)
            one = pygame.Rect(509,234,274,562 )
            two = pygame.Rect(595,236,650,275)
            three = pygame.Rect(680,234,738,277)
            four = pygame.Rect(510,307,554,350)
            five = pygame.Rect(594,306,651,350)
            six = pygame.Rect(651,350,679,306)
            seven = pygame.Rect(507,374,417,564)
            eight = pygame.Rect(593,374,649,416)
            nine = pygame.Rect(680,374,734,414)
            zero = pygame.Rect(592,437,647,481)
            hash = pygame.Rect(681,443,736,484)


            if one.collidepoint(event.pos):
                self.code += "1"
            elif two.collidepoint(event.pos):
                self.code += "2"
            
            elif three.collidepoint(event.pos):
                self.code += "3"
            
            elif four.collidepoint(event.pos):
                self.code += "4"
            
            elif five.collidepoint(event.pos):
                self.code += "5"
            
            elif six.collidepoint(event.pos):
                self.code += "6"
            
            elif seven.collidepoint(event.pos):
                self.code += "7"
            
            elif eight.collidepoint(event.pos):
                self.code += "8"
            
            elif nine.collidepoint(event.pos):
                self.code += "9"
            elif zero.collidepoint(event.pos):
                self.code += "0"
            ##I understand this is horrible practice but i can't think straight right now i should be multiplying and for looping this.
           
            elif hash.collidepoint(event.pos):
                self.code = []
            print(self.code)

