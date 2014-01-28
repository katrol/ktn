from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server and call it mailserver
mailserver = "smtp.samfundet.no" #Fill in

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
serverPort = 25
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, serverPort))
# Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand =  'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# send MAIL FROM command and print server response.
# Fill in start
mailfrom = 'MAIL FROM: katrine@roland.tw\r\n'
clientSocket.send(mailfrom)
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
    print '250 reply not received from server.'
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptto = 'RCPT TO: katrinro@samfundet.no\r\n'
clientSocket.send(rcptto)
recv3 = clientSocket.recv(1024)
print recv3
if recv3[:3] != '250':
    print '250 reply not received from server.'
# Fill in end

# Send DATA command and print server response
# Fill in start
clientSocket.send('DATA\r\n')
recv4 = clientSocket.recv(1024)
print recv4
if recv4[:3] != '354':
    print '354 reply not received from server.'
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg)
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg)
recv5 = clientSocket.recv(1024)
print recv5
if recv5[:3] != '250':
    print '250 reply not received from server.'
# Fill in end

# Send QUIT command and get server response.
# Fill in start
clientSocket.send('QUIT\r\n')
recv6 = clientSocket.recv(1024)
print recv6
if recv6[:3] != '221':
    print '221 reply not received from server.'
# Fill in end
