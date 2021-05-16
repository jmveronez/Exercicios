#Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. 
#Se eles forem iguais, imprima que são valores idênticos.

def Menor_Valor(a,b):
    if a < b:
        print(a,"é menor que",b)
    elif b < a:
        print(b,"é menor que",a)
    elif a == b:
        print("Estes valores são idênticos")

str_a = int(input("Digite um valor: "))
str_b = int(input("Digite outro valor: "))

Menor_Valor(str_a,str_b)