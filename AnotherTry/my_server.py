import socket
from threading import Thread
from time import sleep
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 5050
server.bind((host,port))
server.listen(1)
while True:
    client,adr = server.accept()
    print('A client is connected.',adr)
    while True:
        m = client.recv(1024).decode('utf-8')
        print('Received %s'%m)
        sleep(2)
        s = input('Enter something.\n')
        client.sendall(s.encode('utf-8'))