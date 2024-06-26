#import necessary libs
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox, numpy, socket, ctypes, sys
from random import randint
from os import system, name, path, execv
from sys import exit
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0) #hide console window
#define variables
p1 = ''
p2 = ''
mode = ""
s = ''
button1 =''
val = 0
version = 'v0.1.1'
#define funcions
def restart_main():
    # Restart the application...
    executable = sys.executable
    executable_filename = path.split(executable)[1]
    if executable_filename.lower().startswith('python'):
        # application is running within a python interpreter
        python = executable
        execv(python, [python, ] + sys.argv)
        pass
    else:
        # application is running as a standalone executable
        execv(executable, sys.argv)
        pass
    pass
def proper_close() :
    global s
    try:
        s.send("DISCNCT_REQ".encode())
        s.close()
        root.destroy()
    except AttributeError:
        exit(0)
def randoml(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
def disconnect(ipentry, hostentry):
    global s, l2, button1,connect_button
    s.send("DISCNCT_REQ".encode())
    s.close()
    button1.destroy()
    connect_button = ttk.Button(frame2, text="Connect", command= lambda:connect(ipentry, hostentry))
    connect_button.pack(expand=True, pady=10)
    l2.destroy()
    l2 = Label(frame2, text = 'Not Connected!', foreground = '#FF0000')
    l2.pack()
def send(length, n0):
    global mode, p1, p2, s, val
    try:
        mode = int(length.get())
        p1 = int(n0.get())
        p1 = str(n0.get())
    except ValueError:
        tkinter.messagebox.showerror(title="Error", message="Error when verify input.Perhaps you have a typo?")
        return 1
    if len(str(n0.get())) == int(length.get()):
        pass
    else:
        tkinter.messagebox.showerror(message="expected number to be %s character(s) long" %(int(length.get())))
    try:
        if val == 0:
            s.send(str(p1).encode())
        else:
            pass
    except:
        tkinter.messagebox.showerror(message="Seem like that you havent connect to any server yet.\nSwitch to 'Server connection' tab to connect.")
        return 0
    if val == 0:
        while p2 == '':
            p2 = s.recv(1024).decode()
            s.send(str(p1).encode())
    else:
        p2 = randoml(int(length.get()))
    guesskickstart()
def connect(ipentry, portentry):
    global s,l2,button1,connect_button
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    except socket.error as err: 
        tkinter.messagebox.showerror(title="Error when creating socket", message="Socket creation failed with error %s" %(err))
        return 0
    ip = str(ipentry.get())
    port = str(portentry.get())
    try:
        s.connect((ip, int(port)))
        l2.destroy()
        connect_button.destroy()
        button1 = ttk.Button(frame2, text="Disconnect", command= lambda:disconnect(ipentry, hostentry))
        button1.pack(expand=True, pady=10)
        l2 = Label(frame2, text = 'Connected', foreground = '#006800')
        l2.pack()
    except socket.error as err:
        tkinter.messagebox.showerror(title="Error when connecting", message="Connection failed with error %s" %(err))
def logic(inp1, inp2):
    global length
    np1 = numpy.array(list(str(inp1)))
    np2 = numpy.array(list(str(inp2)))
    try:
        correctarr = np1 == np2
        ret = correctarr.sum()
        print(f"{inp1}({ret})")
        if ret == mode:
            print('u win!')
            input("press enter to exit")
            exit(0)
    except ValueError as err:
        tkinter.messagebox.showerror(title="Crashed!", message="Crashed with error:\n%s\nPress OK to restart" %(err))
        restart_main()       
def guesskickstart():
    root.destroy()
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 4)
    guess()
def guess():
    global mode
    x = input("guess: ")
    if len(x) == mode:
        pass
    else:
        guess()
    logic(x, p2)
    guess()
def check_status():
    global val
    if check_var.get() == 0:
        val = 0
        ipentry.config(state= "enabled")
        hostentry.config(state= "enabled")
        connect_button.config(state= "enabled")
    else:
        val = 1
        ipentry.config(state= "disabled")
        hostentry.config(state= "disabled")
        connect_button.config(state= "disabled")
#ui
root = tkinter.Tk()
root.geometry('300x250')
root.title("Crack the number!")
root.resizable(False, False)
Label(root, text = 'CRACK THE NUMBER %s' %(version)).pack()
check_var = tk.IntVar()
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=False)
frame1 = ttk.Frame(notebook, width=550, height=425)
Label(frame1, text = 'Number length').pack()
lengthentry = ttk.Entry(frame1 , justify= 'center')
lengthentry.pack()
Label(frame1, text = 'Number').pack()
numentry = ttk.Entry(frame1 , justify= 'center')
numentry.pack()
send_button = ttk.Button(frame1, text="Start", command= lambda : send(lengthentry, numentry))
send_button.pack(expand=True, pady=10)
frame1.pack(fill='both', expand=True)
frame2 = ttk.Frame(notebook, width=550, height=425)
Label(frame2, text = 'IP Address:').pack()
ipentry = ttk.Entry(frame2 , justify= 'center')
ipentry.pack()
Label(frame2, text = 'Port:').pack()
hostentry = ttk.Entry(frame2 , justify= 'center')
hostentry.pack()
offlinemode = ttk.Checkbutton(frame2,command=lambda : check_status(),variable=check_var,text="Offline Mode")
offlinemode.pack()
connect_button = ttk.Button(frame2, text="Connect", command= lambda:connect(ipentry, hostentry))
connect_button.pack(expand=True, pady=10)
l2 = Label(frame2, text = 'Not Connected!', foreground = '#FF0000')
l2.pack()
frame2.pack(fill='both', expand=True)
notebook.add(frame1, text='Game options')
notebook.add(frame2, text='Server connection')
root.protocol('WM_DELETE_WINDOW', proper_close)
root.mainloop()
