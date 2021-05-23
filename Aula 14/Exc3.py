#03 Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha
#  para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após 
# entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai 
# “pensar” em um número inteiro entre 0 e 20. O jogador vai tentar adivinhar qual número foi escolhido
#  até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou 
# menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

import random

def adivinhacao():
    deducao = 0
    palpites = 0
    resultado = random.randint(1,20)
    deducao = int(input("\nAdivinhe o valor que o computador pensou (1-20): "))
    while deducao != resultado:
        if deducao < 1 or deducao > 20:
            print("\nValor inválido, digite um valor entre 1 e 20!")
        else: 
            if deducao > resultado:
                print("\nQue pena, você errou!")
                print("\nO número digitado é maior que o número pensado!")
            elif resultado > deducao:
                print("\nQue pena, você errou!")
                print("\nO número digitado é menor que o número pensado!")
        deducao = int(input("\nTente novamente: "))
        palpites += 1
        
        print(f"\nParabéns, você acertou depois de {palpites} tentativas!")

senha = "Senha Incorreta"

tentativa = input("Digite a senha para acessar o sistema: ")
i = 1
while tentativa != senha or i != 3:
    if tentativa == senha:
        print("\nAcesso liberado!")
        adivinhacao()
        break
    else:
        tentativa = input("Senha errada, tente novamente: ")
    i += 1
    if i == 3:
        print("ACESSO NEGADO!")
        break