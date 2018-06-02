import socket

SERVER = ('127.0.0.1', 5000)

CONNECTED = False

print 'Connecting to server...'

udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while not CONNECTED:
    udpClient.sendto('PING', SERVER)
    try:
        message, server = udpClient.recvfrom(1024)
    finally:
        if (message == 'PONG'):
            CONNECTED = True

print '...Connection Established'


udpClient.sendto('[:printOptions]', SERVER)

while CONNECTED:
    try:
        message, server = udpClient.recvfrom(1024)
    except socket.timeout:
        print 'REQUEST TIMED OUT => Try Again'
    finally:
        print message
        userInput =  raw_input()
        if(userInput == '3'):
            CONNECTED = False
        udpClient.sendto(userInput, SERVER)

print 'Closing Connection...'
udpClient.close()
print '...Connection Closed!'