# Server program
# when a command is receved from client
# it processes it and sends appropriate result back to client

import socket,threading

IP = ''
PORT = 9999

def executeCommands(client):
    client.send("Enter Commands for eg:  ADD 100 500 ".encode())
    while True:
        ans = 0
        msg = client.recv(50).decode().split()
        cmd = msg[0]
        op1 = int(msg[1])
        op2 = int(msg[2])
        if cmd == "ADD":
            ans = op1 + op2
        elif cmd == "MUL":
            ans = op1*op2
        elif cmd == "SUB":
            ans = op1-op2
        elif cmd == "DIV":
            ans = op1/op2
        elif cmd == "BYE":
            return
        else:
            ans = "INVALID COMMAND"        
        client.send(str(ans).encode())        

def startServer():
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind((IP,PORT))
    server_socket.listen(25)
    print("Server started!")
    while True:
        client,addr=server_socket.accept()
        print(f"client {addr} connected")
        try :
            newThread = threading.Thread(target=executeCommands,args=(client,))
            newThread.start()
        except:
            pass    
        print(f"Client with {addr} starts in new thread.")

if __name__ == '__main__':
    startServer()
