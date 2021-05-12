#Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for 
# negativo e ‘0’ se for 0.

def Valor_Numerico(x):
    if x > 0:
        return "P"
    elif x < 0:
        return "N"
    elif x == 0:
        return "0"
    else:
        return "Valor inválido"

print(Valor_Numerico(1))
print(Valor_Numerico(0))
print(Valor_Numerico(-1))
x = int(input("Digite um valor numérico a ser consultado: "))
print("O valor digitado é:", Valor_Numerico(x))