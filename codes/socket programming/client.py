# Client program 
# when a msg is entered it sends it to server and
# shows the output server has sent

import socket
IP = 'localhost'
PORT = 9999

def enterCommands(client_socket):
    while True:
        msg = client_socket.recv(50).decode()
        print(f"Server sent : {msg}")
        cmd = input()
        if cmd[:3] == "BYE":
            return
        client_socket.send(cmd.encode())

def connectToServer():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((IP,PORT))
    enterCommands(client_socket)

if __name__=="__main__":
    connectToServer()    
