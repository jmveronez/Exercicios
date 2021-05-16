#Escreva uma função que recebe dois números (a e b) como parâmetro e retorna 
#True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite

def soma(a,b,limite):
    asoma = a+b
    if asoma > limite:
        print("True")
        return True
    else:
        print("False")
        return False

str_a = int(input("Digite um valor: "))
str_b = int(input("Digite o segundo valor: "))
str_limite = int(input("Digite o limite da soma: "))

soma(str_a,str_b,str_limite)