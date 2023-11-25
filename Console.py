import pygame
import window


class Console(window.window):

    def __init__(self):
        self.cTxt = ["Console v1.0"]    # Console Text
        self.cLine = "> "               # Console line (current)
        self.consoleScreen = pygame.display.set_mode((800, 600))

    def display(self, screen):
        self.consoleScreen.fill((0, 0, 0))
        font = pygame.font.Font(None, 32)
        tmp = "\r\n".join(self.cTxt) + "\r\n" + self.cLine
        txtSurf = font.render(tmp, True, (255, 255, 255))

        self.consoleScreen.blit(txtSurf, (10, 10))
        pygame.display.flip()

        pass

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
                self.cTxt = self.cTxt[:-1]
            else:
                self.cLine += event.unicode

    def processCmd(self, cmd):
        pass
