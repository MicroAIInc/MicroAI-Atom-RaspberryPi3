#pip3 install html2text
#Usage: python3 terminal-browser.py 

import requests, os, time
from sys import stdout

class colors:
        def __init__(self):
                self.blue = "\033[94m"
                self.red = "\033[91m"
                self.end = "\033[0m"
cl = colors()

try: 
        import html2text

except:
        print("packages not found.. installing....")
        os.system("sudo pip3 install html2text")
        
import html2text
def get_request(url):
    req_get = requests.get(url)
    cont = str(req_get.content, "utf-8")
    if len(cont) == 0:
        if req_get.status_code == 200:
            print (html2text.html2text(cont))
        elif req_get.status_code == 404:
            print ("Error 404, Not Found!")
        elif req_get.status_code == 500:
            print ("Error 500, Internal server error!")
        else:
            print (html2text.html2text(cont))

    # If non-empty content is detected, print it.
    # This is to allow customised html error messages.
    else:
        print (html2text.html2text(cont))


def main():
    print ("A python terminal web browser\n")
    print("")
    print (cl.blue+"Trying to browse onetech.ai"+cl.end)
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
    get_request("https://www.onetech.ai")
    print("")
    print (cl.blue+"Trying to browse plasmacomp.com"+cl.end)
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
    get_request("https://www.plasmacomp.com")
    print (cl.blue+"Trying to browse gmail.com"+cl.end)
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
    get_request("https://www.gmail.com")
    
'''
    while True:
        link = "http://"+input("URL: ")
        if link == "quit":
            break
        else:
            pass

        get_request(link)
'''

if __name__ == "__main__":
    main()
