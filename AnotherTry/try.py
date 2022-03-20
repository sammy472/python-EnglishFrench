from time import sleep
from my_client import counter

while True:
    counter = counter+1
    print(counter)
    sleep(2)
