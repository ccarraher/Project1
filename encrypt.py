import sys
password = ""

def setPassword(arg):
    global password
    password = arg

def generateKey(string):
    key = list(password)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -len(key)):
            key.append(key[i % len(key)])
    return("".join(key))

def encrypt(arg):
    # Vigenere cypher
    key = generateKey(arg)
    encrypt_text = []
    for i in range(len(arg)):
        x = (ord(arg[i]) +ord(key[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return ("".join(encrypt_text))

def decrypt(arg):
    # Vigenere cypher
    key = generateKey(arg)
    orig_text = []
    for i in range(len(arg)):
        x = (ord(arg[i]) -ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("".join(orig_text))

def parseCommand(command, arg):
    if(command == "PASSKEY"):
        if(arg != ""):
            setPassword(arg)
            print("PASSWORD")
            print("Password successfully set")
            sys.stdout.flush()
        else:
            print("ERROR")
            print("Try again and enter a string for your password")
            sys.stdout.flush()
    elif(command == "ENCRYPT"):
        if(password == ""):
            print("ERROR")
            print("Password is not set")
            sys.stdout.flush()
        else:
            encryptedText = encrypt(arg)
            print("RESULT")
            print(encryptedText)
            sys.stdout.flush()
    elif(command == "DECRYPT"):
        if(password == ""):
            print("ERROR")
            print("Password is not set")
            sys.stdout.flush()
        else:
            decryptedText = decrypt(arg)
            print("RESULT")
            print(decryptedText)
            sys.stdout.flush()

command = sys.stdin.readline().rstrip()
arg = sys.stdin.readline().rstrip()
while command != "QUIT":
    if (command != "" and arg != ""):
        parseCommand(command, arg)
        command = sys.stdin.readline().rstrip()
        arg = sys.stdin.readline().rstrip()