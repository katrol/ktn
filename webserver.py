# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

# prepare a server socket
# Fill in start

serverSocket.bind(('',1337))
serverSocket.listen(1)

# Fill in end

while True:
    # Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept() # Fill in

    try:
        message = connectionSocket.recv(1024) # Fill in
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() # Fill in

        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            print outputdata[i]
            connectionSocket.send(outputdata[i])
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send("404 Not Found\r\n\r\n")
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
