#Desenvolva um código em Python que gere um número aleatório de 1 a 100 e dê ao usuário 10 chances 
# para acertá-lo. A cada tentativa, deve ser impressa a quantidade de tentativas restantes e 
# se o número aleatório é maior ou menor do que o número inserido na tentativa atual. 
# Se o usuário não acertar em 10 tentativas, informe qual o número aleatório. 
# [Dica: use a função randint para gerar o número aleatório]

import random

resultado = random.randint(1,100)

i = 10

while i >= 1:
    i = i - 1
    n = int(input("Tente descobrir o número mágico (entre 1 e 100): "))
    if n > resultado:
        print("O número mágico é menor, tente novamente!")
    elif n < resultado:
        print("O número mágico é maior, tente novamente!")
    else:
        print("Acertou, o número mágico é:",resultado,":D")
        break
    print("Você ainda tem",i,"tentativas")

if i == 0:
    print("Que pena, você perdeu :(")
    print("O resultado seria:",resultado)