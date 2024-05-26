import numpy, socket
from os import system, name
p1 = ''
p2 = 51890 
mode = ""
def check(inp,lim):
    if len(str(inp)) == lim:
        pass
    else:
        print(f"expected number to be {mode} character(s) long")
        start()

def logic(inp1, inp2):
    np1 = numpy.array(list(str(inp1)))
    np2 = numpy.array(list(str(inp2)))
    correctarr = np1 == np2
    ret = correctarr.sum()
    print(f"{inp1}({ret})")
def clearscr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def guess():
    global mode
    x = input("guess: ")
    if len(x) == mode:
        pass
    else:
        guess()
    logic(x, p2)
    guess()
def socketint():
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print ("Socket successfully created")
    except socket.error as err: 
        print ("socket creation failed with error %s" %(err))
    ip = input("Enter ip address: ")
    port = int(input("Enter port: "))
    try:
        s.connect((ip, port))
        s.send('test'.encode())
        print("Connected successfully!")
        print(s.recv(1024).decode())
    except :
        pass
def start():
    global mode, p1
    try:
        mode = int(input("choose how long is your number: "))
        p1 = int(input("choose ur number: "))
    except ValueError:
        clearscr()
        start()
    check(p1,mode)
    clearscr()
    guess()
socketint()
start()

