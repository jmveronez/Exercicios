#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
# A soma deles;
# A multiplicação entre eles;
# A divisão inteira deles;
# Mostre na tela qual é o maior;
# Verifique se o resultado da soma é par ou impar e mostre na tela;
# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e 
# mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

def Calculadora(a,b):
    soma = a+b
    mult = a*b
    div = a/b
    if a > b:
        print(f"O número {a} é maior que o número {b}!")
    elif b > a:
        print(f"O número {b} é maior que o número {a}!")
    else:
        print("Os números são iguais!")
    
    if soma % 2 == 0:
        print("O resultado da soma é PAR!")
    else:
        print("O resultado da soma é ÍMPAR!")

    if mult > 40:
        print (mult/div)
    else:
        print("A multiplicação não é maior que 401")

a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))

Calculadora(a,b)