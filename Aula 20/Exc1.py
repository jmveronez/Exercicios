class Ingresso:
    def __init__(self,ingresso):
        self.ingresso = ingresso

    def ImprimirValor(self):
        return self.ingresso

class IngressoVIP(Ingresso):
    def __init__(self, ingresso, adicional):
        super().__init__(ingresso)
        self.adicional = adicional
    
    def ImprimirValorVIP(self):
        return self.ingresso + self.adicional

ingresso = Ingresso(50)
VIP = IngressoVIP(ingresso.ingresso,45)

print(f"O ingresso para a pista custa R${ingresso.ImprimirValor()}\nO ingresso para o VIP custa R${VIP.ImprimirValorVIP()}")