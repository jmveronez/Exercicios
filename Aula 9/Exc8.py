#Escreva um programa que determine todos os números de 4 algarismos que possam ser separados em 
# dois números de dois algarismos que somados e elevando-se a soma ao quadrado obtenha-se o próprio número.
#Exemplo: 3025 = 55 e 55**2 é igual á 3025

for i in range(1000,10000):
    parte1 = i // 100
    parte2 = i % 100
    if (parte1+parte2)**2 == i:
        print(i)