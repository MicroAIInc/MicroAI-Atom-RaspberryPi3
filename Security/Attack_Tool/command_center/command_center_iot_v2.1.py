import requests
import json
from cfg import cfg

import curses

initiator_url = cfg.target_url

def cmdOut(scr, cmd):
    scr.clear()
    scr.addstr(0,0, 'Attacking...')
    scr.refresh()
    scr.addstr(1,0, '{}' .format(attackOut(cmd)))
    scr.addstr(2,0, 'Presse ANY KEY to continue.')
    scr.refresh()
    key = scr.getch()
    return

#send attack commends out
def attackOut(atk_idx):
    try:
        content = {'attack':atk_idx}
        r = requests.post(url=initiator_url, json=content)
    except:
        return json.dumps({"Message": "Initiator is offline."})
    return r.text

# Application attack menu
def applicationMenu(scr):
    menu_options = [
        '(*) Background',
        '[1] Hash Collision',
        '[2] Clickjacking with CryptoJacking',
        '[3] FakeSSL with CryptoJacking',
        '[4] SQL Injection',
        '[5] XSS - Cross-site Scripting',
        '[6] Broken Authentication',
        '(*) BACK'
    ]
    menu_mapping = {
        0: 'background',
        1: 3, #hash collision
        2: 10,#clickjacking with cryptojacking
        3: 11,#FakeSSL with cryptojacking
        4: 12,#SQL injection
        5: 13,#XSS corss-site scriptin
        6: 14,#broken auth
        7: 'BACK'
    }

    def menuDisplay(scr, selected):
        scr.clear()
        #title
        scr.addstr(0,0, 'Applicatioin Level Attacks')
        for idx, item in enumerate(menu_options):
            if idx == selected:
                scr.attron(curses.color_pair(1))
                scr.addstr(idx+1,0, item)
                scr.attroff(curses.color_pair(1))
                scr.refresh()
            else:
                scr.addstr(idx+1,0, item)
                scr.refresh()
    
    exception = False
    current_row = 0
    menuDisplay(scr, current_row)
    # graceful closing procedure 1, 2, 3, 4, 5
    while True:
        try:
            if exception == True: #3
                break #4
            
            key = scr.getch()
            if key == curses.KEY_UP and current_row > 0: # actions when pressed up key
                current_row -= 1
            elif key == curses.KEY_UP and current_row == 0: # actions when pressed up key when the cursor reached bottom
                current_row = len(menu_options)-1
            elif key == curses.KEY_DOWN and current_row < len(menu_options)-1: # actions when pressed down key
                current_row += 1
            elif key == curses.KEY_DOWN and current_row >= len(menu_options)-1: # actions when pressed down key when cursor reached top
                current_row = 0
            elif key == curses.KEY_BACKSPACE or key==curses.KEY_LEFT:
                break
            # actions when pressed enter key
            elif key == curses.KEY_ENTER or key==curses.KEY_RIGHT or key in [10, 13]:
                if menu_mapping[current_row]=='BACK':
                    break
                elif menu_mapping[current_row]=='background':
                    scr.clear()
                    scr.addstr(0,0,  'Application Level Attack')
                    # text source: https://ccdcoe.org/library/publications/application-level-attacks-study/
                    scr.addstr(2,0,  'An application-layer attack targets computers by deliberately causing a fault in a')
                    scr.addstr(3,0,  'computer’s operating system or applications. This results in the attacker gaining')
                    scr.addstr(4,0,  'the ability to bypass normal access controls. The attacker takes advantage of this')
                    scr.addstr(5,0,  'situation, gaining control of an application, system or network. Application-level')
                    scr.addstr(6,0,  'attacks can be performed either on a server or a client computer. The key difference')
                    scr.addstr(7,0,  'from other types of attacks, such as network traffic eavesdropping/tampering, is the')
                    scr.addstr(8,0,  'ability of the attacker to be active (up to having total control over the compromised')
                    scr.addstr(9,0,  'machine, rather than passively looking at the network traffic that happens to occur')
                    scr.addstr(10,0, 'at any given time.')
                    scr.addstr(12,0, 'Source: NATO Cooperative Cyber Defence Centre of Excellence')
                    scr.addstr(14,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()

                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='placeholder':
                    scr.clear()
                    scr.addstr(0,0, 'Placeholder')
                    scr.addstr(1,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                else: #actual option
                    cmdOut(scr, menu_mapping[current_row])
                #cmdOut(main_screen, current_row)
                #break
            menuDisplay(scr, current_row)
            
        except KeyboardInterrupt: #1
            exception = True #2
    return


def networkMenu(scr):
    menu_options = [
        '(*) Background',
        '[1] Denial of Service Attacks',
        '[2] Man In The Middle',
        '(*) BACK'
    ]
    menu_mapping = {
        0: 'background',
        1: 'DoS',
        2: 'MITM',
        3: 'BACK'
    }
    def menuDisplay(scr, selected):
        scr.clear()
        #title
        scr.addstr(0,0, 'Network Level Attacks')
        for idx, item in enumerate(menu_options):
            if idx == selected:
                scr.attron(curses.color_pair(1))
                scr.addstr(idx+1,0, item)
                scr.attroff(curses.color_pair(1))
                scr.refresh()
            else:
                scr.addstr(idx+1,0, item)
                scr.refresh()
    exception = False
    current_row = 0
    menuDisplay(scr, current_row)
    # graceful closing procedure 1, 2, 3, 4, 5
    while True:
        try:
            if exception == True: #3
                break #4
            
            key = scr.getch()
            if key == curses.KEY_UP and current_row > 0: # actions when pressed up key
                current_row -= 1
            elif key == curses.KEY_UP and current_row == 0: # actions when pressed up key when the cursor reached bottom
                current_row = len(menu_options)-1
            elif key == curses.KEY_DOWN and current_row < len(menu_options)-1: # actions when pressed down key
                current_row += 1
            elif key == curses.KEY_DOWN and current_row >= len(menu_options)-1: # actions when pressed down key when cursor reached top
                current_row = 0
            elif key == curses.KEY_BACKSPACE or key==curses.KEY_LEFT: #use backspace key to back up menu
                break
            # actions when pressed enter key
            elif key == curses.KEY_ENTER or key==curses.KEY_RIGHT or key in [10, 13]:
                if menu_mapping[current_row]=='BACK':
                    break
                elif menu_mapping[current_row]=='background':
                    scr.clear()
                    scr.addstr(0,0,  'Network Level Attacks')
                    # text source: https://www.akamai.com/us/en/resources/network-attacks.jsp
                    scr.addstr(2,0,  'Network security attacks are unauthorized actions against private, corporate or')
                    scr.addstr(3,0,  'governmental IT assets in order to destroy them, modify them or steal sensitive')
                    scr.addstr(4,0,  'data. As more enterprises invite employees to access data from mobile devices,')
                    scr.addstr(5,0,  'networks become vulnerable to data theft or total destruction of the data or network.')
                    scr.addstr(6,0,  '')
                    scr.addstr(7,0,  'There are two main types of network attacks:')
                    scr.addstr(8,0,  'Passive: this is when sensitive information is screened and monitored, potentially')
                    scr.addstr(9,0,  'compromising the security of enterprises and their customers.')
                    scr.addstr(10,0, 'Active: this is when information is altered by a hacker or destroyed entirely.')
                    scr.addstr(12,0, 'Source: Akamai Technologies')
                    scr.addstr(14,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()

                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='DoS':
                    DOSMenu(scr)
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='MITM':
                    mitmMenu(scr)
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                #placeholder for testing purpose
                if menu_mapping[current_row]=='placeholder':
                    scr.clear()
                    scr.addstr(0,0, 'Placeholder')
                    scr.addstr(1,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                else: #actual option
                    cmdOut(scr, menu_mapping[current_row])
                #cmdOut(main_screen, current_row)
                #break
            menuDisplay(scr, current_row)
            
        except KeyboardInterrupt: #1
            exception = True #2
    return

# Denial of Service menu within Network attack menu
def DOSMenu(scr):
    menu_options = [
        '(*)  Background',
        '[1]  SYN Flood',
        '[2]  ICMP Flood',
        '[3]  Ping Of Death',
        '[4]  Slow Loris',
        '[5]  ACK Flood',
        '[6]  UDP Flood',
        '[7]  DNS Flood',
        '[8]  Water Torture DNS Flood',
        '[9]  Teardrop DoS',
        '[10] GRE IP Flood',
        '[11] GRE ETH Flood',
        '[12] STOMP Flood',
        '[13] HTTP GET Flood',
        '[14] Smuf DoS Attak',
        '(*)  BACK'
    ]
    menu_mapping = {
        0: 'background',
        1: 6,  #SYN flood
        2: 20, #ICMP flood
        3: 21, #Ping of Death
        4: 22, #slow loris
        5: 23, #ACK flood
        6: 24, #UDP flood
        7: 25, #DNS flood
        8: 26, #water torture
        9: 27, #Teardrop
        10:28, #GRE IP flood
        11:29, #GRE ETH flood
        12:30, #STOMP floods
        13:31, #HTTP GET flood
        14:36, #Smurf DoS
        15:'BACK'
    }

    def menuDisplay(scr, selected):
        scr.clear()
        #title
        scr.addstr(0,0, 'Denial of Service Attacks')
        for idx, item in enumerate(menu_options):
            if idx == selected:
                scr.attron(curses.color_pair(1))
                scr.addstr(idx+1,0, item)
                scr.attroff(curses.color_pair(1))
                scr.refresh()
            else:
                scr.addstr(idx+1,0, item)
                scr.refresh()
    
    exception = False
    current_row = 0
    menuDisplay(scr, current_row)
    # graceful closing procedure 1, 2, 3, 4, 5
    while True:
        try:
            if exception == True: #3
                break #4
            
            key = scr.getch()
            if key == curses.KEY_UP and current_row > 0: # actions when pressed up key
                current_row -= 1
            elif key == curses.KEY_UP and current_row == 0: # actions when pressed up key when the cursor reached bottom
                current_row = len(menu_options)-1
            elif key == curses.KEY_DOWN and current_row < len(menu_options)-1: # actions when pressed down key
                current_row += 1
            elif key == curses.KEY_DOWN and current_row >= len(menu_options)-1: # actions when pressed down key when cursor reached top
                current_row = 0
            elif key == curses.KEY_BACKSPACE or key==curses.KEY_LEFT: #use backspace key to back up menu
                break
            # actions when pressed enter key
            elif key == curses.KEY_ENTER or key==curses.KEY_RIGHT or key in [10, 13]:
                if menu_mapping[current_row]=='BACK':
                    break
                elif menu_mapping[current_row]=='background':
                    scr.clear()
                    scr.addstr(0,0,  'Denial of Service Attacks')
                    # text source: https://www.cloudflare.com/learning/ddos/glossary/denial-of-service/
                    scr.addstr(2,0,  'A denial-of-service (DoS) attack is a type of cyber attack in which a malicious actor')
                    scr.addstr(3,0,  'aims to render a computer or other device unavailable to its intended users by interrupting')
                    scr.addstr(4,0,  'the device\'s normal functioning. DoS attacks typically function by overwhelming or flooding')
                    scr.addstr(5,0,  'a targeted machine with requests until normal traffic is unable to be processed, resulting')
                    scr.addstr(6,0,  'in denial-of-service to addition users. A DoS attack is characterized by using a single')
                    scr.addstr(7,0,  'computer to launch the attack.')
                    scr.addstr(8,0,  'A distributed denial-of-service (DDoS) attack is a type of DoS attack that comes from many')
                    scr.addstr(9,0,  'distributed sources, such as a botnet DDoS attack.')
                    scr.addstr(11,0, 'Source: Cloudflare, Inc.')
                    scr.addstr(13,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()

                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='placeholder':
                    scr.clear()
                    scr.addstr(0,0, 'Placeholder')
                    scr.addstr(1,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                else: #actual option
                    cmdOut(scr, menu_mapping[current_row])
                #cmdOut(main_screen, current_row)
                #break
            menuDisplay(scr, current_row)
            
        except KeyboardInterrupt: #1
            exception = True #2
    return



# Man in the Middle 
def mitmMenu(scr):
    menu_options = [
        '(*)  Background',
        '[1]  ARP-Posoning',
        '[2]  ARP-Poisoning (Internet DoS)',
        '[3]  ARP-Poisoning + SSL-Strip',
        '[4]  ARP-Poisoning + HTTP Sniffer',
        '[5]  ARP-Poisoning + MySql Sniffer Attack',
        '(*)  BACK'
    ]
    menu_mapping = {
        0: 'background',
        1: 32, #ARP-Poisoning attack
        2: 33, #ARP-Poisoning (Internet DoS) attack
        3: 35, #ARP-Poisoning + SSL-Strip attack
        4: 34, #ARP-Poisoning + HTTP Sniffer attack
        5: 37, #DB ARP-Poisoning + MySql sniffer attack
        6:'BACK'
    }

    def menuDisplay(scr, selected):
        scr.clear()
        #title
        scr.addstr(0,0, 'Man in The Middle Attack')
        for idx, item in enumerate(menu_options):
            if idx == selected:
                scr.attron(curses.color_pair(1))
                scr.addstr(idx+1,0, item)
                scr.attroff(curses.color_pair(1))
                scr.refresh()
            else:
                scr.addstr(idx+1,0, item)
                scr.refresh()
    
    exception = False 
    current_row = 0
    menuDisplay(scr, current_row)
    # graceful closing procedure 1, 2, 3, 4, 5
    while True:
        try:
            if exception == True: #3
                break #4
            
            key = scr.getch()
            if key == curses.KEY_UP and current_row > 0: # actions when pressed up key
                current_row -= 1
            elif key == curses.KEY_UP and current_row == 0: # actions when pressed up key when the cursor reached bottom
                current_row = len(menu_options)-1
            elif key == curses.KEY_DOWN and current_row < len(menu_options)-1: # actions when pressed down key
                current_row += 1
            elif key == curses.KEY_DOWN and current_row >= len(menu_options)-1: # actions when pressed down key when cursor reached top
                current_row = 0
            elif key == curses.KEY_BACKSPACE or key==curses.KEY_LEFT: #use backspace key to back up menu
                break
            # actions when pressed enter key
            elif key == curses.KEY_ENTER or key==curses.KEY_RIGHT or key in [10, 13]:
                if menu_mapping[current_row]=='BACK':
                    break
                elif menu_mapping[current_row]=='background':
                    scr.clear()
                    scr.addstr(0,0,  'Man In The Middle Attacks')
                    # text source: https://www.imperva.com/learn/application-security/man-in-the-middle-attack-mitm/
                    scr.addstr(2,0,  'A man in the middle (MITM) attack is a general term for when a perpetrator positions')
                    scr.addstr(3,0,  'himself in a conversation between a user and an application—either to eavesdrop or to')
                    scr.addstr(4,0,  'impersonate one of the parties, making it appear as if a normal exchange of information')
                    scr.addstr(5,0,  'is underway.')
                    scr.addstr(7,0,  'The goal of an attack is to steal personal information, such as login credentials, account')
                    scr.addstr(8,0,  'details and credit card numbers. Targets are typically the users of financial applications,')
                    scr.addstr(9,0,  'SaaS businesses, e-commerce sites and other websites where logging in is required.')
                    scr.addstr(11,0, 'Source: Imperva, Inc,')
                    scr.addstr(13,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()

                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='placeholder':
                    scr.clear()
                    scr.addstr(0,0, 'Placeholder')
                    scr.addstr(1,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                else: #actual option
                    cmdOut(scr, menu_mapping[current_row])
                #cmdOut(main_screen, current_row)
                #break
            menuDisplay(scr, current_row)
            
        except KeyboardInterrupt: #1
            exception = True #2
    return




def systemMenu(scr):
    menu_options = [
        '(*) Background',
        '[1] Abnormal CPU Usage',
        '[2] Abnormal Memory Usage',
        '[3] Crypto Jacking',
        '[4] Ransomware',
        '[5] Data Siphon',
        '[6] Password Cracking',
        '[7] Backdoor',
        '[8] USB Hacking',
        '[9] I/O Attack',
        '(*) BACK'
    ]
    menu_mapping = {
        0: 'background',
        1: 4, #abnormal cpu
        2: 5, #abnormal ram
        3: 1, #crypto jacking
        4: 9, #ransomeware
        5: 0, #data siphon
        6: 2, #password cracking
        7: 7, #backdoor
        8: 'USB Hacking',
        9: 'I/O Attack',
        10:'BACK'
    }
    def menuDisplay(scr, selected):
        scr.clear()
        #title
        scr.addstr(0,0, 'System Level Attacks')
        for idx, item in enumerate(menu_options):
            if idx == selected:
                scr.attron(curses.color_pair(1))
                scr.addstr(idx+1,0, item)
                scr.attroff(curses.color_pair(1))
                scr.refresh()
            else:
                scr.addstr(idx+1,0, item)
                scr.refresh()
    exception = False
    current_row = 0
    menuDisplay(scr, current_row)
    # graceful closing procedure 1, 2, 3, 4, 5
    while True:
        try:
            if exception == True: #3
                break #4
            
            key = scr.getch()
            if key == curses.KEY_UP and current_row > 0: # actions when pressed up key
                current_row -= 1
            elif key == curses.KEY_UP and current_row == 0: # actions when pressed up key when the cursor reached bottom
                current_row = len(menu_options)-1
            elif key == curses.KEY_DOWN and current_row < len(menu_options)-1: # actions when pressed down key
                current_row += 1
            elif key == curses.KEY_DOWN and current_row >= len(menu_options)-1: # actions when pressed down key when cursor reached top
                current_row = 0
            elif key == curses.KEY_BACKSPACE or key==curses.KEY_LEFT: #use backspace key to back up menu
                break
            # actions when pressed enter key
            elif key == curses.KEY_ENTER or key==curses.KEY_RIGHT or key in [10, 13]:
                if menu_mapping[current_row]=='BACK':
                    break
                elif menu_mapping[current_row]=='background':
                    scr.clear()
                    scr.addstr(0,0,  'System Level Attacks')
                    # text source:
                    scr.addstr(2,0,  'System level attacks aim to disrupt the normal operation of the computer system.')
                    scr.addstr(3,0,  'The attacker could gain access through application, network, or even hardware.')
                    scr.addstr(4,0,  'System level attack can be very dangerous because all applications running on the')
                    scr.addstr(5,0,  'system can potentially be affected.')
                    #scr.addstr(6,0,  'attacks can be performed either on a server or a client computer. The key difference')
                    #scr.addstr(7,0,  'from other types of attacks, such as network traffic eavesdropping/tampering, is the')
                    #scr.addstr(8,0,  'ability of the attacker to be active (up to having total control over the compromised')
                    #scr.addstr(9,0,  'machine, rather than passively looking at the network traffic that happens to occur')
                    #scr.addstr(10,0, 'at any given time.')
                    scr.addstr(7,0,  'Source: OneTech, Inc.')
                    scr.addstr(9,0,  'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()

                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='USB Hacking':
                    scr.clear()
                    scr.addstr(0,0,  'USB Attack Instruction')
                    scr.addstr(2,0,  'What You Will Need:')
                    scr.addstr(3,0,  '    - one USB Rubber Ducky (includes a microSD card)')
                    scr.addstr(4,0,  '    - a microSD card adapter or USB card reader to load files to the Ducky')
                    scr.addstr(5,0,  'Steps:')
                    scr.addstr(6,0,  '1 - Download the Duck Encoder or use the web interface:')
                    scr.addstr(7,0,  '    https://ducktoolkit.com/encode')
                    scr.addstr(8,0,  '    https://github.com/hak5darren/USB-Rubber-Ducky/blob/master/duckencoder.jar')
                    scr.addstr(9,0,  '    In order to create the Ducky payloads, we need to have the duck encoder installed.')
                    scr.addstr(10,0, '    This is a program that takes our script and converts it into a cross-platform inject.bin ')
                    scr.addstr(11,0, '    file that the keyboard adapter will use to deliver our keystroke payload.')
                    scr.addstr(12,0, '')
                    scr.addstr(13,0, '2 - Insert the microSD card into your computer:')
                    scr.addstr(14,0, '3 - Get your payload from the folder usb_attack_payload')
                    scr.addstr(15,0, '4 - Encode the payload via the encoder and create inject.bin file.')
                    scr.addstr(16,0, '5 - Transfer "inject.bin" to the microSD card.')
                    scr.addstr(17,0, '6 - Test the USB on the target machine!')
                    scr.addstr(18,0, '')
                    scr.addstr(20,0,  'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='I/O Attack':
                    scr.clear()
                    scr.addstr(0,0,  'IO Attack Instruction')
                    scr.addstr(2,0,  'You need a Raspberry Pi 3 and a motion sensor.')
                    scr.addstr(3,0,  'Follow this instruction to connect the motion sensor to your Raspberry Pi:')
                    scr.addstr(4,0,  '    - https://tutorials-raspberrypi.com/connect-and-control-raspberry-pi-motion-detector-pir/')
                    scr.addstr(5,0,  'Steps:')
                    scr.addstr(6,0,  '1 - Locate "motionsensor_hack_backdoor.py" in "IO_hack" folder.')
                    scr.addstr(7,0,  '2 - Run "motionsensor_hack_backdoor.py"')
                    scr.addstr(8,0,  '3 - Wait 60 seconds for the sensor to warm up.')
                    scr.addstr(9,0,  '4 - When you want to trigger the attack, keep waving your hand in front of the motion')
                    scr.addstr(10,0,  '    sensor, making sure it always shows "motion detected" for at least one minute')
                    scr.addstr(11,0, '4 - A backdoor will be opened on your system now')
                    scr.addstr(12,0, '5 - Use command "nc <ip of victim> <port of victim>" on another machine to connect to')
                    scr.addstr(13,0, '    the backdoor.')
                    scr.addstr(15,0,  'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='placeholder':
                    scr.clear()
                    scr.addstr(0,0, 'Placeholder')
                    scr.addstr(1,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                else: #actual option
                    cmdOut(scr, menu_mapping[current_row])
                #cmdOut(main_screen, current_row)
                #break
            menuDisplay(scr, current_row)
            
        except KeyboardInterrupt: #1
            exception = True #2
    return



def normalMenu(scr):
    menu_options = [
        '(*) Background',
        '[1] Compress & Decomrpess files',
        '[2] P2P Download',
        '[3] Image Processing',
        '[4] Web Browsing',
        '[5] Gaming',
        '(*) BACK'
    ]
    menu_mapping = {
        0: 'background',
        1: 15, #compress & decompress files
        2: 16, #P2P download
        3: 17, #Image Processing
        4: 18, #web browsing
        5: 19, #gaming
        6: 'BACK'
    }
    def menuDisplay(scr, selected):
        scr.clear()
        #title
        scr.addstr(0,0, 'Normal Behaviors')
        for idx, item in enumerate(menu_options):
            if idx == selected:
                scr.attron(curses.color_pair(1))
                scr.addstr(idx+1,0, item)
                scr.attroff(curses.color_pair(1))
                scr.refresh()
            else:
                scr.addstr(idx+1,0, item)
                scr.refresh()
    exception = False
    current_row = 0
    menuDisplay(scr, current_row)
    # graceful closing procedure 1, 2, 3, 4, 5
    while True:
        try:
            if exception == True: #3
                break #4
            
            key = scr.getch()
            if key == curses.KEY_UP and current_row > 0: # actions when pressed up key
                current_row -= 1
            elif key == curses.KEY_UP and current_row == 0: # actions when pressed up key when the cursor reached bottom
                current_row = len(menu_options)-1
            elif key == curses.KEY_DOWN and current_row < len(menu_options)-1: # actions when pressed down key
                current_row += 1
            elif key == curses.KEY_DOWN and current_row >= len(menu_options)-1: # actions when pressed down key when cursor reached top
                current_row = 0
            elif key == curses.KEY_BACKSPACE or key==curses.KEY_LEFT: #use backspace key to back up menu
                break
            # actions when pressed enter key
            elif key == curses.KEY_ENTER or key==curses.KEY_RIGHT or key in [10, 13]:
                if menu_mapping[current_row]=='BACK':
                    break
                elif menu_mapping[current_row]=='background':
                    scr.clear()
                    scr.addstr(0,0,  'Normal Behaviors')
                    # text source:
                    scr.addstr(2,0,  'We provided a list of simulated normal behaviors in our tool.')
                    scr.addstr(4,0,  'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()

                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='placeholder':
                    scr.clear()
                    scr.addstr(0,0, 'Placeholder')
                    scr.addstr(1,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()
                    #go back go normal
                    menuDisplay(scr, current_row)
                    continue
                else: #actual option
                    cmdOut(scr, menu_mapping[current_row])
                #cmdOut(main_screen, current_row)
                #break
            menuDisplay(scr, current_row)
            
        except KeyboardInterrupt: #1
            exception = True #2
    return



def IoTMenu(scr):
    menu_options = [
        '(*) Ping Initiator',
        '[1] Application Level Attack',
        '[2] Network Level Attack',
        '[3] System Level Attack',
        '[4] Normal Behaviors',
        '(*) EXIT',
    ]
    menu_mapping = {
        0: 'Initiator', #initiator
        1: 'Application',
        2: 'Network',
        3: 'System',
        4: 'Normal',
        5: 'EXIT'
    }

    def menuDisplay(scr, selected):
        scr.clear()
        #title
        scr.addstr(0,0, 'OneTech IoT Cyber Attack Simulation Tool')
        #scr.addstr(8,0, 'ENTER     : Confirm your choice.')
        #scr.addstr(9,0, 'ARROW keys: Cycle through options. ')
        #scr.addstr(10,0,'BACKSPACE : Go back')
        for idx, item in enumerate(menu_options):
            if idx == selected:
                scr.attron(curses.color_pair(1))
                scr.addstr(idx+1,0, item)
                scr.attroff(curses.color_pair(1))
                scr.refresh()
            else:
                scr.addstr(idx+1,0, item)
                scr.refresh()

    exception = False
    current_row = 0
    menuDisplay(scr, current_row)
    # graceful closing procedure 1, 2, 3, 4, 5
    while True:
        try:
            if exception == True: #3
                break #4
            
            key = scr.getch()
            if key == curses.KEY_UP and current_row > 0: # actions when pressed up key
                current_row -= 1
            elif key == curses.KEY_UP and current_row == 0: # actions when pressed up key when the cursor reached bottom
                current_row = len(menu_options)-1
            elif key == curses.KEY_DOWN and current_row < len(menu_options)-1: # actions when pressed down key
                current_row += 1
            elif key == curses.KEY_DOWN and current_row >= len(menu_options)-1: # actions when pressed down key when cursor reached top
                current_row = 0
            elif key == curses.KEY_BACKSPACE or key==curses.KEY_LEFT: #use backspace key to back up menu
                break
            # actions when pressed enter key
            elif key == curses.KEY_ENTER or key==curses.KEY_RIGHT or key in [10, 13]:
                if menu_mapping[current_row]=='EXIT':
                    break
                if menu_mapping[current_row]=='Initiator':
                    init_status = attackOut('ping')
                    if init_status == '{"Message": "Initiator is offline."}':
                        scr.clear()
                        scr.addstr(0,0, '[!] Initiator is offline.')
                        scr.addstr(1,0, '[?] Troubleshoot:')
                        scr.addstr(2,0, '[?] Have you started initiator?')
                        scr.addstr(3,0, '[?] Do you have the correct target_url in cfg.py?')
                        scr.addstr(4,0, 'Presse ANY KEY to continue.')
                        scr.refresh()
                        scr.getch()
                        #go back to normal
                        menuDisplay(scr, current_row)
                        continue
                        
                    elif init_status == '{"Message": "Initiator is online."}':
                        scr.clear()
                        scr.addstr(0,0, '[*] Initiator is online.')
                        scr.refresh()
                        curses.napms(1500)
                        #go back to normal
                        menuDisplay(scr, current_row)
                        continue
                #debugging
                if menu_mapping[current_row]=='Application':
                    applicationMenu(scr)
                    #go back to normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='Network':
                    networkMenu(scr)
                    #go back to normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='System':
                    systemMenu(scr)
                    #go back to normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='Normal':
                    normalMenu(scr)
                    #go back to normal
                    menuDisplay(scr, current_row)
                    continue
                if menu_mapping[current_row]=='placeholder':
                    scr.clear()
                    scr.addstr(0,0, 'Placeholder')
                    scr.addstr(1,0, 'Presse ANY KEY to continue.')
                    scr.refresh()
                    scr.getch()
                #else: #actual option
                #    cmdOut(main_screen, menu_mapping[current_row])
            menuDisplay(scr, current_row)
            
        except KeyboardInterrupt: #1
            exception = True #2



def main():
    exception=False
    current_row = 0
    screen = curses.initscr()
    curses.start_color()
    curses.use_default_colors() #needed if want to use default color
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.curs_set(0)
    curses.cbreak()
    curses.noecho()
    screen.keypad(1) #important if want use arrow keys
    
    IoTMenu(screen) #start main menu

    curses.nocbreak()   # Turn off cbreak mode
    curses.echo()       # Turn echo back on
    curses.curs_set(1)  # Turn cursor back on
    screen.keypad(0) # Turn off keypad keys, If initialized like `my_screen = curses.initscr()`
    curses.napms(1)
    curses.endwin() #5
    
    
if __name__ == '__main__':
    main()