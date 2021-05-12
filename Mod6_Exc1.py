#1.	Faça um programa, com uma função que necessite de três argumentos,
#  e que forneça a soma desses três argumentos

a = int(input("Digite o primeiro valor a ser somado: "))
b = int(input("Digite o segundo valor a ser somado: "))
c = int(input("Digite o terceiro valor a ser somado: "))

def soma(a,b,c):
    return a+b+c

print("O valor total da soma é de: ", soma(a,b,c))