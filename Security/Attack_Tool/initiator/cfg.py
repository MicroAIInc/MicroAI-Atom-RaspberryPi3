class cfg:
    
    #Initiator
    initiator_ip = '0.0.0.0' #set it to 0.0.0.0 to allow it to listen to command from the network
    initiator_port = 11000 #which port will listen to the command
    
    #loadCPU
    cpu_cores = 4 #will not exceeds total cores available
    cpu_load_time = 6 #seconds. will not exceeds 60 seconds
    
    #CryptoJackiing Configuration
    mining_difficulty = 18 #integer. expoential. small increase make it much harder. 18 works well with raspberry pi 3. 
    num_of_blocks_to_mine = 5 #integer
 
    #Data Siphon
    siphon_repeat = 3 #integer. how many times to repeat data siphon simulation
    siphon_wait = 10 #in seconds. wait period between data siphon
    
    #hashcrackig
    max_length = 5 #the maximum length of password that password cracking bruteforce attack will attempt to crack.
                   #Set this number higher if you wnat to try longer passphrases.
                   #Be aware the diffculty grows exponentially as the passphrase gets longer. 
    
    collision_difficulty = 5 #integer. exponential. small increase will make it much harder

    #Clickjacking
    clickjacking_timer = 10 #integer. This will allow you to run the clickjacking for a chosen amount of time

    #fakessl
    fakessl_timer= 30 #integer. This will allow you to run the fakessl for a chosen amount of time

    #p2p download
    p2pdownload_timer= 10 #integer. This will allow you to run the p2p download for a chosen amount of time
    
    #DOS configuration
    dos_target = '127.0.0.1' #The ip address of the target
    dos_interface= 'lo' #default interface
    dos_port = 8080 #destination port
    dos_thread_limit = 2 #number of threads
    dos_duration = 20 #in seconds.
    smurf_attack_zombie_ip = '255.255.255.255' #Here is the broadcast ip address of the target, you need to change this in smurf attack only. 


    #Man In The Middle Attack configuration
    mitm_target = '192.168.2.131' #The ip address of the target
    mitm_duration = 10 #in seconds.