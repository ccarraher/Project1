import sys
password = ""

def setPassword(arg):
    global password
    password = arg

def encrypt(arg):
    # Vigenere cypher
    cipher_text = []
    for i in range(len(arg)):
        x = (ord(arg[i]) +
             ord(password[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def decrypt(arg):
    # Vigenere cypher
    orig_text = []
    for i in range(len(arg)):
        x = (ord(arg[i]) -
             ord(password[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

def parseCommand(command, arg):
    if(command == "PASSKEY"):
        setPassword(arg)
    elif(command == "ENCRYPT"):
        if(password == ""):
            print("ERROR\n")
            print("Password is not set\n")
        encryptedText = encrypt(arg)
        print("RESULT\n")
        print(encryptedText + "\n")
        sys.stdout.flush()
    elif(command == "DECRYPT"):
        if(password == ""):
            print("ERROR\n")
            print("Password is not set\n")
        decryptedText = decrypt(arg)
        print("RESULT\n")
        print(decryptedText + "\n")
        sys.stdout.flush()

command = sys.stdin.readline().rstrip()
arg = sys.stdin.readline().rstrip()
while command != "QUIT":
    if (command != "" and arg != ""):
        parseCommand(command, arg)
        command = sys.stdin.readline().rstrip()
        arg = sys.stdin.readline().rstrip()