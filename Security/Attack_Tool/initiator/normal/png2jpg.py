#The following script will enable you to convert images from jpeg format to PNG format. 
#Usage: python3 jpg2png.py
from PIL import Image
import time, subprocess, os
from sys import stdout

class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()

def main():
    dirctory = os.path.dirname(__file__)
    print("")
    print (cl.blue+"Converting photo.png to JPG"+cl.end)
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
    try:
        im = Image.open(os.path.join(dirctory, "photo.png"))
        im.save('/tmp/PNGPhoto.jpg')
        print("PNGPhoto.jpg has been generated successfully")
    except:
        print("Couldn't convert image")
        
        
    try:
        time.sleep(1)
        print("")
        print(cl.blue+"Removing processed files ......"+cl.end)
        subprocess.run('rm /tmp/PDFPhoto.pdf', shell=True)
        subprocess.run('rm /tmp/photo.thumbnail', shell=True)
        subprocess.run('rm /tmp/PNGPhoto.jpg', shell=True)
        time.sleep(2)
        print("Done....")
    except:
       print("Couldn't remove files")

if __name__=='__main__':
    main()