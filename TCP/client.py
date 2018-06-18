import socket
import sys

SERVER = ('192.168.0.104', 5000)

print 'Connecting to server...'

tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    tcpClient.connect(SERVER)
except socket.error as err_msg:
    print 'Unable to instantiate socket. Error code: %d, Error message: %s' % (err_msg[0], err_msg[1])
    sys.exit(1)
finally:
    print '...Connection Established'

print 'To Exit press <CTRL + X> and <ENTER>'

while True:
    try:
        message = tcpClient.recv(1024)
    except socket.timeout:
        print 'REQUEST TIMED OUT => Try Again'
    finally:
        print message
        userInput =  raw_input()
        if(userInput == '\x18'):
            break
        tcpClient.send(userInput)

print 'Closing Connection...'
tcpClient.close()
print '...Connection Closed!'