import uuid
import random
from rich.console import Console
from time import sleep
import socket
from rich.progress import track
from rich.console import Console
from time import sleep
import random
import uuid
from datetime import date


console = Console()
hacker = "green"
hostname = socket.gethostname()
IpAddress = socket.gethostbyname(hostname)
Domaine = socket.gethostbyaddr(hostname)
Dns = Domaine[0]
rand_value = random.randint(0,5)
id = uuid.uuid4()
today = date.today()


class Protocol_Socket():

    # Output using rich setting
    def Protocol():
        protocol = socket.getprotobyname(hostname)
        return protocol
    try:
        Protocol()
    except:
        console.print("Analysing...", style=hacker)
        sleep(2)
        for step in track(range(10)):
            for i in range(10):
                rand_value = random.randint(0,1)
            step
            sleep(rand_value)

        console.print("Found!!",style=hacker)
        sleep(1)
        console.print("Analysing...\n" , style=hacker)
        for step in track(range(100)):
            sleep(0.07)
            step
        console.print("Cracking!!", style=hacker)
        for step in track(range(100)):
            sleep(0.05)
            step

console.print("Success!! ", style=hacker)

sleep(2)

print('''\033[1;32;40m \n

01010110010100100111001010010010010010010010 

| |    | |   /\   /  ___| |  / /____| |    \ 
| |____| |  /  \ /  /   | | / /_____  |     |
|  ____  | / /\ \| |    | |/\_______| |     |
| |    |  / ____ \ \____| |\ \______  |     |
| |    | /_/    \_\_____| | \_\_____|_|____/

01010110010100100111001010010010010010010010  

\n''')

sleep(3)


def infinite_loop():
   
    # generate infinite uuid loop
    while True:
        id = str(uuid.uuid4())
        randomed_id = id[:random.randint(0, len(id) - 1)]
        #- random space
        spaces = " " * random.randint(0,100)

        console.print(spaces, randomed_id,style=hacker)
   

infinite_loop()
