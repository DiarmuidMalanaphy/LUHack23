import pygame
import window
import time


class Console(window.window):

    def __init__(self):
        self.cTxt = []      # Console Text
        self.cLine = "> "     # Console line (current)

    def show(self, screen):
        border = pygame.Rect(0, 0, 800, 600)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.cTxt.append(self.cLine)
                        self.processCmd(self.cLine)
                        self.cLine = "> "
                    elif event.key == pygame.K_TAB:
                        # Autocomplete?
                        pass
                    elif event.key == pygame.K_BACKSPACE:
                        self.cTxt = self.cTxt[:-1]
                    else:
                        self.cLine += event.unicode
            screen.fill((0, 0, 0))

            font = pygame.font.Font(None, 32)

            tmp = "\n".join(self.cTxt) + "\n" + self.cLine
            print(tmp)
            txtSurf = font.render(tmp, True, (255, 255, 255))

            screen.blit(txtSurf, (10, 10))
            pygame.display.flip()
            time.sleep(0.01)

    def processCmd(self, cmd):
        pass
