from letter import letter
from title import title
from Console import Console

class windowManager():
    
    def __init__(self,currentWindow):
        self.currentWindow = currentWindow
        self.previousWindowList = []
    
    def getCurrentWindow(self):
        return(self.currentWindow)
    
    def changeCurrentWindow(self,result): #pass result as a tuple  {back?,window}
        if result is not None:
            print(result[0])
            
            if result[0]:
                self.currentWindow = self.previousWindowList.pop()
            else:
                self.previousWindowList.append(self.currentWindow)
                self.currentWindow = result[1]
                
                
            