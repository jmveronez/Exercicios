#02 Utilizando estruturas de repetição com variável de controle, faça um programa que receba
#  uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u 
# e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

def vogais(frase):
    vogais = 0
    vogais_1 = "AEIOUÁÀÃÂÉÈÊÓÒÔÕÚÙÛÍÌÎ"
    palavra_alterada = frase
    for letra in frase:
        if letra.upper() in vogais_1:
            vogais += 1

    for letra in palavra_alterada:
        if letra.upper() in vogais_1:
            palavra_alterada = palavra_alterada.replace(letra,"")
    print(f"A frase ou palavra {frase} possui {vogais} vogais e fica {palavra_alterada} sem elas")

frase = input("Digite uma frase ou palavra e veja a mágica acontecer: ")

vogais(frase)