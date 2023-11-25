

from PIL import Image
class window:
    
    def display(self, screen):#override this and implement it yourself
        raise Exception ("Implement yourself")
    def check_event(self,event):
        raise Exception ("Implement yourself")
    
    def previous_window(self,previousWindow):
        window = previousWindow

    def resize(self,input_path,size):

        with Image.open(input_path) as img:
            # Resize the image
            img = img.resize(size, Image.ANTIALIAS)

            # Save the resized image
        return(img)