class Conta():
    def __init__(self  ,titular,numero,saldo):
        self.titular = titular
        self.numero = numero
        self._saldo = saldo
    
    @property    
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self,saldo):
        if saldo<0:
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo 
    
    def saque(self,valor):
        if self._saldo>=valor:
            self._saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("saldo insuficiente")       
                   
    def depositar(self,valor):
        self._saldo += valor    
        
    def extrato(self):
        print("Cliente: ",self._titular,"Saldo Atual:", self._saldo)    