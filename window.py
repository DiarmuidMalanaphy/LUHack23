


class window:
    
    def display(self, screen):#override this and implement it yourself
        raise Exception ("Implement yourself")
    def check_event(self,event):
        raise Exception ("Implement yourself")
    
    def previous_window(self,previousWindow):
        window = previousWindow

    