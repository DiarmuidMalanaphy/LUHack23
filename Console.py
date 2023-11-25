import pygame
import window
import time


class Console(window.window):

    def __init__(self):
        self.cTxt = ["Server Console"]    # Console Text
        self.cLine = "> "               # Console line (current)
        self.width = 800
        self.height = 600
        self.consoleScreen = pygame.display.set_mode((self.width, self.height))

    def add2Console(self, lines):
        for line in lines:
            self.cTxt.append(line)
        self.display()

    def display(self, screen):
        self.consoleScreen.fill((0, 0, 0))
        # font = pygame.font.Font("Monospace", 32)
        font = pygame.font.Font(None, 32)

        lineGap = 8         # Pixels between each line
        _, fonth = font.size("a")

        self.cTxt.reverse()

        y = self.height - 10 + lineGap
        linew, lineh = font.size(self.cLine)
        # If the line length is less than window width
        if linew < self.width - 20:
            y -= fonth+lineGap
            screen.blit(font.render(self.cLine, True, (255, 255, 255)), (10, y))
        else:
            sLine = [""]      # Split lines
            currLine = 0
            for c in self.cLine:
                w, h = font.size(sLine[currLine] + " ")
                if w >= self.width-20:
                    currLine += 1
                    sLine += [""]
                sLine[currLine] += c
            sLine.reverse()
            for j in sLine:
                y -= fonth + lineGap
                screen.blit(font.render(j, True, (255, 255, 255)), (10, y))

        # Console Text
        for i in range(len(self.cTxt)):
            line = self.cTxt[i]
            linew, lineh = font.size(line)

            # If the line length is less than window width
            if linew < self.width - 20:
                y -= fonth+lineGap
                screen.blit(font.render(line, True, (255, 255, 255)), (10, y))
                continue

            sLine = [""]      # Split lines
            currLine = 0
            for c in line:
                w, h = font.size(sLine[currLine] + " ")
                if w >= self.width-20:
                    currLine += 1
                    sLine += [""]
                sLine[currLine] += c
            sLine.reverse()
            for j in sLine:
                y -= fonth + lineGap
                screen.blit(font.render(j, True, (255, 255, 255)), (10, y))

        self.cTxt.reverse()

        time.sleep(0.01)

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.cTxt.append(self.cLine)
                self.processCmd(self.cLine)
                self.cLine = "> "
            elif event.key == pygame.K_TAB:
                # Autocomplete?
                pass
            elif event.key == pygame.K_BACKSPACE:
                if len(self.cLine) != 2:
                    self.cLine = self.cLine[:-1]
            else:
                self.cLine += event.unicode

    def processCmd(self, cmd):
        pass
