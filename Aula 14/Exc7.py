#07 Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
# lista única que mantenha separados os valores pares e ímpares. 
# No final, mostre os valores pares e ímpares em ordem crescente.


def classificacao():
    pares = []
    impares = []
    v1 = int(input("Digite o primeiro valor: "))
    if v1 % 2 == 0 :
        pares.append(v1)
    else:
        impares.append(v1)

    v2 = int(input("Digite o segundo valor: "))
    if v2 % 2 == 0 :
        pares.append(v2)
    else:
        impares.append(v2)

    v3 = int(input("Digite o terceiro valor: "))
    if v3 % 2 == 0 :
        pares.append(v3)
    else:
        impares.append(v3)

    v4 = int(input("Digite o quarto valor: "))
    if v4 % 2 == 0 :
        pares.append(v4)
    else:
        impares.append(v4)

    v5 = int(input("Digite o quinto valor: "))
    if v5 % 2 == 0 :
        pares.append(v5)
    else:
        impares.append(v5)
    
    v6 = int(input("Digite o sexto valor: "))
    if v6 % 2 == 0 :
        pares.append(v6)
    else:
        impares.append(v6)
    
    v7 = int(input("Digite o sétimo valor: "))
    if v7 % 2 == 0 :
        pares.append(v7)
    else:
        impares.append(v7)
    
    pares.sort()
    impares.sort()
    print(f"Os valores pares são {pares} e os impares são {impares}!")

classificacao()