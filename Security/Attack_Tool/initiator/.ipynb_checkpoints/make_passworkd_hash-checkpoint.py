import hashlib


pass_phrase = '3dZp' #Password phrase you want the password cracking attack to crack.
                     #Pleaes do no use special characters as we did not count for them
                     #This attack is for demo and testing purpose only.

def hashPassphrase():
    print('[*] Hashing custome password phrase...')
    with open('hashcracking/pass_hash.txt', 'w') as f:
        f.write(hashlib.md5(pass_phrase.encode()).hexdigest())
    print('[*] Password phrase "{}" is hashed.' .format(pass_phrase))
    print('[*] Password hash is stored at "hashcracking/pass_hash.txt".')
    return

if __name__ == '__main__':
    hashPassphrase()