import socket
from serverUtils import Utils

SERVER = ('172.20.10.4', 80)

serverFunctions = Utils()

try:
    udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpServer.bind(SERVER)
except socket.error as err_msg:
    print 'Unable to instantiate socket. Error code: %d, Error message: %s' % (err_msg[0], err_msg[1])
    sys.exit(1)

print 'Server Status => RUNING & LISTENING | on => %s | Port => %d' % (SERVER[0], SERVER[1])

while True:
    message, client = udpServer.recvfrom(1024)
    print message
    if message == 'PING':
        udpServer.sendto('PONG', client)
    else:
        serverFunctions.decideAndExecFunc(message, client, udpServer)


print 'Shutting Server Down...'
udpServer.close()
print '...Server is Down!'