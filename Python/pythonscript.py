import sys
import socket
from datetime import date

NAME = sys.argv[1]
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
BUILD_DATE = date.today()
REV_NAME = NAME[::-1]
CHAR_NAME = len(NAME)

if NAME == "Anonymous":
    print("You didnt enter your name")
    print("So I'll call you", NAME)
    print("But.. I know your IP:", IPAddr)
    print("Your computer Name is:", hostname)
    print("And you exicute this script in:", BUILD_DATE)
    print("Bye for now, and dont forget, Python is the best!")
else:
    print("Hi you!")
    print("Your name is:", NAME)
    print("Your name in reversed:", REV_NAME)
    print("Characters number in your name:", CHAR_NAME)
    print("Your IP is:", IPAddr)
    print("Your computer Name is:", hostname)
    print("And you exicute this script in:", BUILD_DATE)
    print("Bye for now, and dont forget, Python is the best!")
