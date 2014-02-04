from socket import *
from datetime import *
from time import time

ip = "192.168.1.141"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

for i in range(10):
    start = time()
    message = "Ping " + str(i) + " " + datetime.now().strftime("%H:%M:%S")
    clientSocket.sendto(message, (ip, serverPort))

    try:
        response, serverAdress = clientSocket.recvfrom(1024)
        responsetime = time()
        print response
        rtt = responsetime - start
        print "RTT: " + str(rtt)

    except timeout:
        print "Request timed out"
         

