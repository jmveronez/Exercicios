#06 Utilizando listas faça um programa que faça 5 perguntas para uma pessoa 
# sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

SIM = []

resposta1 = input("Telefonou para a vítima?\n")
if resposta1.upper() == "SIM":
    SIM.append(resposta1)

resposta2 = input("Esteve no local do crime?\n")
if resposta2.upper() == "SIM":
    SIM.append(resposta2)

resposta3 = input("Mora perto da vítima?\n")
if resposta3.upper() == "SIM":
    SIM.append(resposta3)

resposta4 = input("Devia para a vítima?\n")
if resposta4.upper() == "SIM":
    SIM.append(resposta4)

resposta5 = input("Já trabalhou com a vítima?\n")
if resposta5.upper() == "SIM":
    SIM.append(resposta5)

if len(SIM) == 5:
    print("\n\nAssasino!")
elif len(SIM) == 3 or len(SIM) == 4:
    print("\n\nCúmplice!")
elif len(SIM) == 2:
    print("\n\nSuspeita!")
else:
    print("\n\nInocente!")