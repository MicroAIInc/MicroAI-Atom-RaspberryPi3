import os

# IoT attack
try: 
        import bottle

except:
        print("bottle not found.. installing....") 
        os.system("pip3 install bottle==0.12.17")


try: 
        import twisted

except:
        print("twisted not found.. installing....") 
        os.system("pip3 install twisted")
        os.system("pip3 install pyOpenSSL")
        os.system("pip3 install service_identity")

try: 
        import tqdm

except:
        print("tqdm not found.. installing....") 
        os.system("pip3 install tqdm==4.32.1")

try: 
        import psutil

except:
        print("psutil not found.. installing....") 
        os.system("pip3 install psutil")

try: 
        import html2text

except:
        print("html2text not found.. installing....")
        os.system("pip3 install html2text")

try: 
        import libtorrent as lt

except:
        print("libtorrent not found.. installing....")
        os.system("sudo apt-get install -y python3-libtorrent")
        
try: 
        import mysql.connector

except:
        print("mysql.connector not found.. installing....")
        os.system("pip3 install mysql-connector")

try: 
        import pyshark

except:
        print("pyshark not found.. installing....")
        os.system("pip3 install pyshark==0.4.2.9")


# data base attack
try: 
        import pymysql

except:
        print("pymysql not found.. installing....")
        os.system("pip3 install PyMySQL")

        
try:
       print("Checking other dependencies...")
       os.system("sudo apt-get install -y tcpdump")
       os.system("sudo apt-get install -y tshark")
       os.system("sudo apt-get install -y php")
       #os.system("sudo apt-get install -y mysql-client") #x86_64
       os.system("sudo apt-get install -y mariadb-client") #raspberry pi
       os.system("sudo apt install php7.3-mysql")
       
except Exception as e:
       print(e)

