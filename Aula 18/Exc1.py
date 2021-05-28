class BombaCombustivel:
    def __init__(self,TipoCombustivel,ValorLitro,QuantidadeCombustivel,Caixa):
        self.TipoCombustivel = TipoCombustivel
        self.ValorLitro = ValorLitro
        self.QuantidadeCombustivel = QuantidadeCombustivel
        self.ValorTotal = 0.00
        self.Caixa = Caixa

    def AbastecerPorValor(self, Valor):
        QuantidadeAbastecida = Valor / self.ValorLitro
        if QuantidadeAbastecida > self.QuantidadeCombustivel:
            print("Quantidade indisponível.")
        else:
            self.QuantidadeCombustivel -= QuantidadeAbastecida
            print(f"{QuantidadeAbastecida:.2f} litros abastecido com sucesso, agora temos {self.QuantidadeCombustivel:.2f} litros na bomba!")
            self.Caixa += Valor
    
    def AbastecerPorQuantidade(self,Quantify):
        if Quantify > self.QuantidadeCombustivel:
            print("Quantidade indisponível.")
        else:
            self.QuantidadeCombustivel -= Quantify
            print(f"{Quantify:.2f} litros abastecido com sucesso, agora temos {self.QuantidadeCombustivel:.2f} litros na bomba!")
            self.ValorTotal = self.ValorLitro * Quantify
            print(f"A conta ficou R${self.ValorTotal}!")
            self.Caixa += self.ValorTotal
    
    def AlterarValor(self,New_Value):
        self.ValorLitro = New_Value
    
    def AlterarCombustivel(self, Gass):
        self.TipoCombustivel += Gass
    
    def AlterarQuantidade(self, New_qtd):
        self.QuantidadeCombustivel = New_qtd

if(__name__ == "__main__"):
    tipo = input("Digite o tipo do combustível: ")
    valor = float(input("Digite o valor do combustível: R$"))
    quantidade = float(input("Digite a quantidade de combustível na bomba: "))
    caixa = float(input("Digite o caixa total do posto: R$"))
    Bomba_Combustivel = BombaCombustivel(tipo,valor,quantidade,caixa)
    while True:
        print('-=-'*15)
        print("Ações:")
        print("1 - Visualizar Valores.")
        print("2 - Alterar valor do combustível.")        
        print("3 - Alterar quantidade do combustível.")
        print("4 - Alterar o tipo do combustível.")
        print("5 - Abastecer por um valor específico.")
        print("6 - Abastecer por uma quantidade desejada.")
        print("0 - Sair do sistema!")
        print('-=-'*15)
        acao = int(input("Digite a opção desejada: "))
        if acao == 0:
            break
        elif acao == 1:
            print(f"Você tem R${Bomba_Combustivel.Caixa} de caixa\n{Bomba_Combustivel.QuantidadeCombustivel:.2f}L de combustível {Bomba_Combustivel.TipoCombustivel} à R${Bomba_Combustivel.ValorLitro} o L!")
            continue
        elif acao == 2:
            Novo_Valor = float(input("Digite o novo valor do Combustível: ").replace(",","."))
            Bomba_Combustivel.AlterarValor(Novo_Valor)
            continue
        elif acao == 3:
            Nova_qtd = float(input("Digite a quantidade de combustível que será adicionado ao galão: ").replace(",","."))
            Bomba_Combustivel.AlterarQuantidade(Nova_qtd)
            continue
        elif acao == 4:
            Combustivel = input("Digite qual o novo tipo do combustível: ")
            Bomba_Combustivel.AlterarCombustivel(Combustivel)
            continue
        elif acao == 5:
            Valor = float(input("Digite o valor a ser abastecido: R$").replace(",","."))
            Bomba_Combustivel.AbastecerPorValor(Valor)
            continue
        elif acao == 6:
            Quantidade = float(input("Digite a quantidade que será abastecida: ").replace(",","."))
            Bomba_Combustivel.AbastecerPorQuantidade(Quantidade)
            continue
        else:
            acao = int(input("Digite um valor entre 0 e 6!"))
            continue

