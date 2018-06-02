from pycpfcnpj import cpfcnpj
from datetime import datetime, date

class Utils:

    def __init__ (self):
        self.clientsUsingOptionCPF = []
        self.clientsUsingOptionDataNasc = []
        self.menuOptions = "Estas Sao as Funcionalidades Disponiveis:\n" \
                            "1 - Verificar CPF\n" \
                            "2 - Verificar se a pessoa e maior de idade atraves da data de nascimento\n" \
                            "3 - Terminar a interacao entre cliente e servidor"


    def echo (self, someString):
        return someString


    def checkCPF (self, cpf):
        if cpfcnpj.validate(cpf) == True:
            return 'CPF Valido'
        else:
            return 'CPF Invalido'


    def checkDataNascimento (self, bornDate):
        today = date.today()
        try:
            born = datetime.strptime(bornDate, '%d/%m/%Y')
        except:
            return 'Data Invalida'
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if age >= 18:
            return 'Maior de Idade'
        else:
            return 'Menor de Idade'

    def decideAndExecFunc (self, message, client, server):
        if client in self.clientsUsingOptionCPF:
            server.sendto(self.checkCPF(message), client)
            self.clientsUsingOptionCPF.remove(client)

        elif client in self.clientsUsingOptionDataNasc:
            server.sendto(self.checkDataNascimento(message), client)
            self.clientsUsingOptionDataNasc.remove(client)

        elif message == '[:printOptions]':
            server.sendto(self.menuOptions, client)

        elif message == '1':
            self.clientsUsingOptionCPF.append(client)
            server.sendto('Informe o CPF a ser verificado com ou sem pontuacao', client)
        
        elif message == '2':
            self.clientsUsingOptionDataNasc.append(client)
            server.sendto('Informe a Data a ser verificada <dia/mes/ano>', client)

        else:
            server.sendto('Opcao Desconhecida', client)
