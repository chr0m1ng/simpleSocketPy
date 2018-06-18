import socket
import thread
from serverUtils import Utils

SERVER = ('192.168.0.104', 5000)

serverUtils = Utils()

def client_connected(con, client):
    status = 0 
    print 'Connected with', client
    con.send('Envie o primeiro numero da operacao')
    while status == 0:
        while status == 0:
            num1 = con.recv(1024)
            if not num1 or num1 == '\x18': 
                status = -1
            if serverUtils.RepresentsNumber(num1):
                status = 1
            else:
                con.send('Nao eh um numero, tente novamente... envie o primeiro numero da operacao')
        con.send('Envie o segundo numero da operacao')
        while status == 1:
            num2 = con.recv(1024)
            if not num2 or num2 == '\x18': 
                status = -1
            if serverUtils.RepresentsNumber(num2):
                status = 2
            else:
                con.send('Nao eh um numero, tente novamente... envie o segundo numero da operacao')
        con.send('Escolha uma das operacoes disponiveis:\n%s' % (serverUtils.OperationsToString()))
        while status == 2:
            oper = con.recv(1024)
            if not oper or oper == '\x18': 
                status = -1
            if serverUtils.RepresentsOperation(oper):
                status = 3
            else:
                con.send('Nao eh uma operacao listada, tente novamente...\n%s' % (serverUtils.OperationsToString()))
        
        if status == 3:
            con.send('Resultado: %s\nEnvie o primeiro numero da operacao' % (serverUtils.DoTheMath(num1 + oper + num2)))
            status = 0
        
    print 'Closing connection with client ', client
    con.close()
    thread.exit()

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcpServer.bind(SERVER)
tcpServer.listen(1)

while True:
    con, client = tcpServer.accept()
    thread.start_new_thread(client_connected, tuple([con, client]))

tcpServer.close()