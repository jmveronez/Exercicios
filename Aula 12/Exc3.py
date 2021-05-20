# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo sa estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado

i = int
boletim = dict()

while i != 0:

    boletim['aluno'] = input("Digite o nome do aluno: ")
    boletim['media'] = float(input("Digite a media final do aluno: "))
    if boletim['media'] > 7:
        boletim['resultado'] = "Aprovado"
    elif boletim['media'] < 7 and boletim['media'] >= 5:
        boletim['resultado'] = "Recuperação"
    else:
        boletim['resultado'] = "Reprovado"
    i = int(input("Caso tenha outro aluno para cadastrar digite 1, se não digite 0: "))

for a,b in boletim.items():
    print(f'{a} tem o valor {b}')
