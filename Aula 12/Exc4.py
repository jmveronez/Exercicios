# Crie um programa em que 4 jogadores, joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário
# em ordem, sabendo que o vencedor tirou o maior número no dado.
#Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator

import random,time,operator
lista = []

for i in range(1,6):
    jogador = 1
    dado = random.randint(1,20)
    lista.append([f'jogador{i}'])