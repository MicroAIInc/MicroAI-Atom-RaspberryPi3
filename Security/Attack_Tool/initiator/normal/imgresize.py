#The following script will allow you to resize an image to a specefic dimensions. The default values are: 128, 128
#Usage: python3 imgresize.py photo.jpg
import os, sys, time
from sys import stdout
from PIL import Image

class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()
def main():
    dirctory = os.path.dirname(__file__)
    print("")
    print (cl.blue+"Resizing photo.png to 128*128 pixels "+cl.end)
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    time.sleep(.200)
    stdout.write('.')
    print("")
    
    size = 128, 128
    infile= os.path.join(dirctory, "photo.png")
    outfile = "/tmp/photo.thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
            print("photo.png has been resized successfully")
        except IOError:
            print ("cannot create thumbnail for '%s'" % infile)
    

if __name__=='__main__':
    main()