import sys
from subprocess import Popen, PIPE
from tkinter import E

logger = Popen(['python', 'logger.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
encrypt = Popen(['python', 'encrypt.py'], stdout=PIPE, stdin=PIPE, encoding='utf8')
history = []

fileInput = input("Enter a log file name: ")

logger.stdin.write("file\n")
logger.stdin.write(fileInput + "\n")

def showHistory():
    for i in range(len(history)):
        print(str(i) + ". " + history[i])

# Sorry this is ugly, definitely could be abstracted into a function or two but I don't have time
def parseCommand(command):
    if command == "password":
        option = input("Enter 1 to type new password or 2 to choose from history: ")
        if option == "1":
            arg = input("Enter new password: ")
            history.append(arg)
        elif option == "2" and len(history) > 0:
            showHistory()
            historyInput = input("Enter the number corresponding to the string you'd like for your password: ")
            arg = history[int(historyInput)]
        elif option == "2" and len(history) == 0:
            print("Error: No history exists yet please again with a new input")
        
        logger.stdin.write("PASSWORD\n")
        logger.stdin.write("Password set to " + arg + "\n")

        encrypt.stdin.write("PASSKEY\n")
        encrypt.stdin.write(arg + "\n")
    elif command == "encrypt":
        option = input("Enter 1 to type new encryption string or 2 to choose from history: ")
        if option == "1":
            arg = input("Enter new encryption string: ")
            history.append(arg)
        elif option == "2":
            showHistory()
            historyInput = input("Enter the number corresponding to the string you'd like for your password: ")
            arg = history[int(historyInput)]
        elif option == "2" and len(history) == 0:
            print("Error: No history exists yet please again with a new input")
        logger.stdin.write("ENCRYPT\n")
        logger.stdin.write("Encrypt message set to " + arg + "\n")

        encrypt.stdin.write("ENCRYPT\n")
        encrypt.stdin.write(arg + "\n")
        encrypt.stdin.flush()
        e = encrypt.stdout.readline().rstrip()
        m = encrypt.stdout.readline().rstrip()
        logger.stdin.write(e + "\n")
        logger.stdin.write(m + "\n")
    elif command == "decrypt":
        option = input("Enter 1 to type new decrypt message or 2 to choose from history: ")
        if option == "1":
            arg = input("Enter new decrypt message: ")
            history.append(arg)
        elif option == "2":
            showHistory()
            historyInput = input("Enter the number corresponding to the string you'd like for your password: ")
            arg = history[int(historyInput)]
        elif option == "2" and len(history) == 0:
            print("Error: No history exists yet please again with a new input")
        logger.stdin.write("DECRYPT\n")
        logger.stdin.write("Decrypt message set to " + arg + "\n")

        encrypt.stdin.write("DECRYPT\n")
        encrypt.stdin.write(arg + "\n")
        encrypt.stdin.flush()
        e = encrypt.stdout.readline().rstrip()
        m = encrypt.stdout.readline().rstrip()
        logger.stdin.write(e + "\n")
        logger.stdin.write(m + "\n")
    

        
userInput = input("Enter a command or type help for a list of commands: ")
while userInput != "quit":
    if len(userInput) != 0:
        parseCommand(userInput)
    userInput = input("Enter a command or type help for a list of commands: ")

if userInput == "quit":
    logger.stdin.write("QUIT\n")
    encrypt.stdin.write("QUIT\n")
