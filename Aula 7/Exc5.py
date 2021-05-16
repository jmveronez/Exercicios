#Faça um programa que tenha uma função chamada ficha(),
#  que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome_jogador, gols):
    if gols == 1:
        print(nome_jogador,"marcou",gols,"gol.")
    elif gols == 0:
        print(nome_jogador,"não marcou nenhum gol")
    elif gols > 1:
        print(nome_jogador,"marcou",gols,"gols.")
    else:
        print("Digite um valor válido")

nome_jogador = input("Digite o nome do jogador: ")
gols = int(input("Digite quantos gols ele fez: "))
ficha(nome_jogador,gols)