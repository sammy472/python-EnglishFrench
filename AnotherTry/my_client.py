import socket
from threading import Thread
from time import sleep
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 5050
#client.connect((host,port))
global counter
counter = 0

# while True:
#     s = input('Enter something Buddy\n')
#     client.sendall(s.encode('utf-8'))
#     print('Message sent.\n')
#     sleep(2)
#     m = client.recv(1024).decode('utf-8')
#     print('Received %s\n'%m)
while True:
    counter = counter+1
    print(counter)
    sleep(2)