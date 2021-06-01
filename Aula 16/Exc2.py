class Conta:
    def __init__(self,titular="Eu",saldo=5000):
        self.titular = titular
        self.saldo = saldo
    
    def Sacar(self):
        senha = input("Digite sua senha: ")
        if senha == "Senha_Incorreta":
            sacar = float(input("Digite o quanto gostaria de sacar: R$"))
            if self.saldo > sacar:
                self.saldo -= sacar
                print(f"R${sacar} sacados de sua conta, agora você tem R${self.saldo}!")
            else:
                print("Saldo Insuficiente!")
        else:
            print("Senha Incorreta!")

    def Depositar(self):
        senha = input("Digite sua senha: ")
        if senha == "Senha_Incorreta":
            depositar = float(input("Digite o quanto gostaria de depositar: R$"))
            if depositar > 0:
                self.saldo += depositar
                print(f"R${depositar} depositados em sua conta, agora você tem R${self.saldo}!")
            else:
                print("Números Inválidos!")
        else:
            print("Senha Incorreta!")

conta = Conta()
conta.Sacar()
conta.Depositar()
