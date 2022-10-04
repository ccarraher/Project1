import sys
from datetime import datetime


def getCurrentDateTime():
    today = datetime.now()
    return today

def initLogFile(file):
    f = open(file, "x")
    log("START", "Logging started", file)

def log(action, message, file):
    date = getCurrentDateTime()
    f = open(file, "a")
    f.write(date.strftime("%Y-%m-%d %I:%M") + " " + "[" + action + "]" + " " + message + "\n")

mode = sys.stdin.readline().rstrip()
if mode == "file":
    file = sys.stdin.readline().rstrip()

initLogFile(file)

command = sys.stdin.readline().rstrip()
message = sys.stdin.readline().rstrip()
while command != "QUIT":
    if (command != "" and message != ""):
        log(command, message, file)
        command = sys.stdin.readline().rstrip()
        message = sys.stdin.readline().rstrip()

if command == "QUIT":
    log("QUIT", "Stopping logging", file)