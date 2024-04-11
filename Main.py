
class Main:
    pass
    
from Cliente import Cliente
from Conta import Conta    

if __name__ == '__main':
    c1=Cliente("João", "1232-4343")#instaciando objeto cliente
    conta=Conta(c1._nome,6656,0)#instaciando objeto conta

    print(conta.titular," Numero: ", conta.numero," Seu saldo: ", conta._saldo)

    conta.deposita(100)
    conta.saque(50)
    conta.extrato()

