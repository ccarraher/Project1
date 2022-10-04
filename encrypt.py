import sys
password = ""

def setPassword(arg):
    global password
    password = arg

def encrypt(arg):
    # Vigenere cypher
    key_length = len(password)
    key_as_int = [ord(i) for i in password]
    plaintext_int = [ord(i) for i in arg]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def decrypt(arg):
    # Vigenere cypher
    key_length = len(password)
    key_as_int = [ord(i) for i in password]
    ciphertext_int = [ord(i) for i in arg]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

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