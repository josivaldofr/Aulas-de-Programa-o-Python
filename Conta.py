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
        
        
        