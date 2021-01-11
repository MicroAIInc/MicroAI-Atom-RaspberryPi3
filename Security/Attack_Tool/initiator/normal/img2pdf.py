#The following script will convert image from png to PDF format.
#usage: python3 img2pdf.py
import PIL.Image, time, os
from sys import stdout

class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()


def main():
    dirctory = os.path.dirname(__file__)
    
    print (cl.blue+"Converting photo.png to PDF "+cl.end)
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
        filepath = os.path.join(dirctory, "photo.png")
        newfilename = '/tmp/PDFPhoto.pdf'


        im = PIL.Image.open(filepath)

        im.save(newfilename, "PDF", quality=100)
        print("PDFPhoto.pdf has been generated successfully")
    except:
        print("couldn't convert image")
if __name__=='__main__':
    main()