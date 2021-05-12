#7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.
#  Se eles forem iguais, imprima que eles são iguais.

def Compara_Numero(a,b):
    if a > b:
        print(a,"é o maior número")
    elif b > a:
        print(b,"é o maior número")
    elif a == b:
        print("Os números são iguais")

str_a = float(input("Digite o primeiro valor: "))
str_b = float(input("Digite o segundo valor: "))

Compara_Numero(str_a, str_b)