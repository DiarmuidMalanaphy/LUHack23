import os
import pygame
import window
import time
from packet_Sniffing import packetSniffing


class Console(window.window):

    def __init__(self):
        self.cTxt = ["Server Console"]      # Console Text
        self.prompt = ">"
        self.cLine = self.prompt + " "      # Console line (current)
        self.width = 800
        self.height = 600#
        self.original_size = (pygame.display.get_window_size())
        self.consoleScreen = pygame.display.set_mode((self.width, self.height))
        

    def add2Console(self, lines):
        for line in lines:
            self.cTxt.append(line)
        self.display(self.screen)

    def display(self, screen):
        
        self.screen = screen
        self.consoleScreen.fill((0, 0, 0))
        # font = pygame.font.Font("Monospace", 32)
        font = pygame.font.Font(None, 24)

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
                bool = self.processCmd(self.cLine[2:])
                if bool: # To break the commandline
                    
                    pygame.display.set_mode((self.original_size))
                    try:
                        os.rename('pleasantries.csv','pleasantries1.csv')
                    except:
                        pass
                    return(True,None)
                self.cLine = self.prompt + " "
            elif event.key == pygame.K_TAB:
                # Autocomplete?
                pass
            elif event.key == pygame.K_BACKSPACE:
                if len(self.cLine) != 2:
                    self.cLine = self.cLine[:-1]
            else:
                self.cLine += event.unicode

    def processCmd(self, cmd):
        cmd = cmd.split(" ")
        print(cmd)
        match cmd[0]:
            case "":
                pass
            case "help":
                self.add2Console([
                    "HELP MENU",
                    "    packetSniffer        Prints out a list of packet data to the console, or packets sent by a specific IP",
                    "                                      Usage: packetSniffer %ip%;  E.g. packetSniffer 248.171.41.105",
                    "    exit                       Exits the console"
                    ])
            case "packetSniffer":
                if len(cmd) == 1:
                    pList = packetSniffing().createPacketList()
                    for packet in pList:
                        self.add2Console([packet])
                else:
                    packets = packetSniffing().search(cmd[1])
                    if len(packets) == 0:
                        self.add2Console(["Nothing found!"])
                    else:
                        for packet in packets:
                            self.add2Console([packet])
            case "exit":
                return(True)
            case other:
                self.add2Console(["Command not found! Type \"help\" (without quotes) for more information."])
        pass
