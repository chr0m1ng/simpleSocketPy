class Utils:
    def __init__(self):
        self.operations = ['+', '-', '*', '/']

    def RepresentsInt(self, s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    def RepresentsFloat(self, s):
        try: 
            float(s)
            return True
        except ValueError:
            return False
    
    def RepresentsNumber(self, s):
        return self.RepresentsFloat(s) or self.RepresentsInt(s)

    def RepresentsOperation(self, s):
        return s in self.operations

    def OperationsToString(self):
        return 'Adicao: "+", Subtracao: "-", Produto: "*" e Divisao: "/"'

    def DoTheMath(self, s):
        try:
            res = eval(s)
            return res
        except ZeroDivisionError:
            return 'Impossivel Realizar Divisao por 0'