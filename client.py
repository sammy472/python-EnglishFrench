import socket
import json
import sys
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostbyname(socket.gethostname())
my_port = 9999

# connection to hostname on the port.
# def again_and_again():
#     # s.connect((host, my_port))
#     msg = str(s.recv(1024).decode('utf-8'))
#     answer = str(input(msg))
#     word = str(input('Search...\n'))
#     m = dict(dictionary=answer,word=word)
#     res = json.dumps(m)
#     s.send(bytes(res,encoding='utf-8'))
#     data = s.recv(1024).decode('utf-8')
#     print(data,end='\n')
#     s.close()
global d
d = None
def run_client():
    s.connect((host, my_port))
    while True:
        try:
            lang = input('Enter the language.\n')
            query = input('Enter the query.\n')
            m = dict(lang=lang,word=query)
            m = json.dumps(m)
            s.sendall(bytes(m,encoding='utf-8'))
            data = s.recv(1024).decode('utf-8')
            d = data
            print(d)
        except :
            s.close()
            sys.exit()
if __name__ == '__main__':
    run_client()
    

    
    


        
        

    
    