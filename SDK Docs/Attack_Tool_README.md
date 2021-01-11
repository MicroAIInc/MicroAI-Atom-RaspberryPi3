# OneTech IoT Cyber Attack Simulator
  
## Instruction
1. Start the Initiator python program `initiator.py` with the correct python command.
    - Depending on how you installed your python interpreter, your python command could be `python` or `python3`
        - For example, your command could be `python3 initiator.py`
    - By default, initiator will start at ip 0.0.0.0 and port 11000. This configuration can be changed in cfg.py in the Initiator's folder.
    - Press `Ctrl - C` at anytime to quit.
2. Leaving the Initiator running, start command center `command_center.py`
    - By default, the command center will send attack commands to 'http://127.0.0.1:11000/attack' which is your localhost. This configuration can be changed in cfg.py in the command center folder if your Initiator is running in another machine on the network. Please know the '/attack' at the end of the url is needed regardless of the IP address and port of the target.
3. From the command center, you can choose which attack to simulate on your device. We limited the strength and duration of our attacks to prevent misuse.

## Special Note
- SYN Flood Denial of Service behaves differently with or without an actual victim. It will still work even if you point the attack at an empty IP address. If you want an actual victim, you can start another initiator on another device in your local machine, and aim your attack to your other device by changing the DoS settings in cfg.py
- To explore the backdoor, use another Linux machine as well. When the backdoor is running, use `nc <ip of victim> <port>` to connect to your backdoor. Your backdoor will utilize port **4444**. This port cannot be changed. The IP address of the device running the Initiator is your victim IP.
    
## Requirements
* Required python version: **python3.7**. Other versions of python might not work properly.
* Required python base libraries. They should be pre-installed with official python interpreter installation:
    * json
    * time
    * subprocess
    * os
    * datetime
    * hashlib
    * multiprocessing
    * uuid
    * socket
    * threading
    * itertools
    * string
    * sys
    * random
    * utilities
    * binascii
    * struct
    
    
* Required python 3rd party libraries. Refer to requirements.txt if you have version problems:
    * bottle
    * tqdm