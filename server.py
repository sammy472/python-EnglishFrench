import json
import socket
import sys
import threading
from time import sleep
from wiki import wikipedia_search
from utils import french_to_english,english_to_french
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostbyname(socket.gethostname())
port = 9999
# bind to the port
serversocket.bind((host, port))
# queue up to 5 requests
def handle_client(clientsocket,adr):
    while True:
        try:
            response = json.loads(str(clientsocket.recv(1024).decode('utf-8')))
            if response['lang'] == 'en':
                getAnswer = english_to_french(response['word'])
                if getAnswer != 'does not exist in this dictionary.':
                    clientsocket.send(bytes(getAnswer,encoding='utf-8'))
                else:
                    wiki_response = wikipedia_search(response['word'],'A')
                    clientsocket.sendall(bytes(wiki_response,encoding='utf-8'))
            elif response['lang'] == 'fr':
                getAnswer = french_to_english(response['word'])
                if getAnswer != 'n"existe pas dans cette dictionnaire.':
                    clientsocket.sendall(bytes(getAnswer,encoding='utf-8'))
                else:
                    wiki_response = wikipedia_search(response['word'],'B')
                    clientsocket.sendall(bytes(wiki_response,encoding='utf-8'))
            else:
                clientsocket.sendall(bytes('Got None',encoding='utf-8'))
        except :
            clientsocket.close()
        
counter = 0
def run_server():
    serversocket.listen(10)
    while True:
        #establish a connection
        try:
            clientsocket,addr = serversocket.accept()
            thread = threading.Thread(target=handle_client,args=(clientsocket,addr))
            thread.start()
            print(f'Active Connections {threading.activeCount()-1}')
        except :
            print('Closing the server....')
            sleep(3)
            sys.exit()
run_server()
        



    
   
    
    

