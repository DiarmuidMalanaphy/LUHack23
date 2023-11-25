import pygame
import window
import time


class Console(window.window):

    def __init__(self):
        self.cTxt = ["Console v1.0"]    # Console Text
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
        font = pygame.font.Font(None, 32)

        lineGap = 5         # Pixels between each line
        w, h = font.size("a")
        # Height of all text in console
        cHeight = len(self.cTxt) * (h+lineGap) + h
        # Number of lines to show in terminal
        lines2Show = len(self.cTxt)
        # If height of text in console is higher than window size
        if cHeight >= self.height - 20:
            tmp = 0
            while tmp < self.height - 20:
                lines2Show += 1
                tmp += h + lineGap
            lines2Show -= 1

        self.cTxt.reverse()
        y = self.height - 10 - h
        # Only display last n lines
        screen.blit(font.render(self.cLine, True, (255, 255, 255)), (10, y))
        for line in self.cTxt[:lines2Show]:
            y = y - h - lineGap
            screen.blit(
                font.render(line, True, (255, 255, 255)),
                (10, y)
                )
            # When line exceeds window width
#            linew, lineh = font.size(line)
#            print("lw"+str(linew))
#            if linew >= self.width - 20:
#                currLine = 0
#                lines = []
#                for i in range(len(line)):
#                    clw, _ = font.size(lines[currLine]+" ")
#                    print("hihi" + clw)
#                    if clw >= self.width - 20:
#                        currLine += 1
#                        lines.append("")
#                if lines[-1] == "":
#                    lines.pop(-1)
#                lines.reverse()
#                print(lines)
#                for i in lines:
#                    y -= h + lineGap
#                    screen.blit(
#                        font.render(i, True, (255, 255, 255)),
#                        (10, y)
#                        )
        self.cTxt.reverse()
        # tmp = "\n".join(self.cTxt) + "\n" + self.cLine
        # txtSurf = font.render(tmp, True, (255, 255, 255))

        # self.consoleScreen.blit(txtSurf, (10, 10))
        # pygame.display.flip()

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
