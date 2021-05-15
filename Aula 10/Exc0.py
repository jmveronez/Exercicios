#Crie um laço while que vai pedir para o usuário dois números e faça a soma dos dois. 
# Enquanto a soma não for 50, ele deve continuar repetindo.

a = 0
b = 0
soma = a+b
print("Digite valores que irão resultar em 50")

while soma != 50:
    a = int(input("Digite um valor: "))
    b = int(input("Digite um segundo valor: "))
    soma = a+b
    if soma != 50:
        print("Digite valores que irão resultar em 50, este está dando",soma)
    else:
        print("Finalmente!")