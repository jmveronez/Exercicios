#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o 
# programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
# gabarito da prova assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).  
# Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
#Após todos os alunos terem respondido informar:
#•	Maior e Menor Acerto;
#•	Total de Alunos que utilizaram o sistema;
#•	A Média das Notas da Turma.
# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
#Após concluir isto você poderia incrementar o programa permitindo que o professor 
# digite o gabarito da prova antes dos alunos usarem o programa

gabarito = [["01","A"],["02","B"],["03","C"],["04","D"],["05","E"],["06","E"],["07","D"],["08","C"],["09","B"],["10","A"]]
i = '1'

while i != '0':
    acertos = []
    erros = []
    alunos = []
    maior_nota = []
    menor_nota = []

    alunos.append(input("Digite o nome do aluno: "))

    resp1 = input(f"Digite a resposta da {gabarito[0][0]}ª questão: ")
    while resp1.upper() not in "ABCDE":
        print("Digite um valor válido!")
        resp1 = input(f"Digite a resposta da {gabarito[0][0]}ª questão: ")    
    if resp1.upper() == gabarito[0][1]:
        acertos.append(gabarito[0][0])
    else:
        erros.append(gabarito[0][0])
    
    resp2 = input(f"Digite a resposta da {gabarito[1][0]}ª questão: ")   
    while resp2.upper() not in "ABCDE":
        print("Digite um valor válido!") 
        resp2 = input(f"Digite a resposta da {gabarito[1][0]}ª questão: ")     
    if resp2.upper() == gabarito[1][1]:
        acertos.append(gabarito[1][0])
    else:
        erros.append(gabarito[1][0])
    
    resp3 = input(f"Digite a resposta da {gabarito[2][0]}ª questão: ") 
    while resp3.upper() not in "ABCDE":
        print("Digite um valor válido!")
        resp3 = input(f"Digite a resposta da {gabarito[2][0]}ª questão: ")       
    if resp3.upper() == gabarito[2][1]:
        acertos.append(gabarito[2][0])
    else:
        erros.append(gabarito[2][0])
    
    resp4 = input(f"Digite a resposta da {gabarito[3][0]}ª questão: ") 
    while resp4.upper() not in "ABCDE":
        print("Digite um valor válido!")       
        resp4 = input(f"Digite a resposta da {gabarito[3][0]}ª questão: ") 
    if resp4.upper() == gabarito[3][1]:
        acertos.append(gabarito[3][0])
    else:
        erros.append(gabarito[3][0])

    resp5 = input(f"Digite a resposta da {gabarito[4][0]}ª questão: ")   
    while resp5.upper() not in "ABCDE":
        print("Digite um valor válido!")     
        resp5 = input(f"Digite a resposta da {gabarito[4][0]}ª questão: ")
    if resp5.upper() == gabarito[4][1]:
        acertos.append(gabarito[4][0])
    else:
        erros.append(gabarito[4][0])
    
    resp6 = input(f"Digite a resposta da {gabarito[5][0]}ª questão: ") 
    while resp6.upper() not in "ABCDE":
        print("Digite um valor válido!")   
        resp6 = input(f"Digite a resposta da {gabarito[5][0]}ª questão: ")     
    if resp6.upper() == gabarito[5][1]:
        acertos.append(gabarito[5][0])
    else:
        erros.append(gabarito[5][0])
    
    resp7 = input(f"Digite a resposta da {gabarito[6][0]}ª questão: ") 
    while resp7.upper() not in "ABCDE":
        print("Digite um valor válido!")       
        resp7 = input(f"Digite a resposta da {gabarito[6][0]}ª questão: ")
    if resp7.upper() == gabarito[6][1]:
        acertos.append(gabarito[6][0])
    else:
        erros.append(gabarito[6][0])
    
    resp8 = input(f"Digite a resposta da {gabarito[7][0]}ª questão: ")
    while resp8.upper() not in "ABCDE":
        print("Digite um valor válido!")
        resp8 = input(f"Digite a resposta da {gabarito[7][0]}ª questão: ")        
    if resp8.upper() == gabarito[7][1]:
        acertos.append(gabarito[7][0])
    else:
        erros.append(gabarito[7][0])
    
    resp9 = input(f"Digite a resposta da {gabarito[8][0]}ª questão: ") 
    while resp9.upper() not in "ABCDE":
        print("Digite um valor válido!")
        resp9 = input(f"Digite a resposta da {gabarito[8][0]}ª questão: ")       
    if resp9.upper() == gabarito[8][1]:
        acertos.append(gabarito[8][0])
    else:
        erros.append(gabarito[8][0])
    
    resp10 = input(f"Digite a resposta da {gabarito[9][0]}ª questão: ")   
    while resp10.upper() not in "ABCDE":
        print("Digite um valor válido!")
        resp10 = input(f"Digite a resposta da {gabarito[9][0]}ª questão: ")     
    if resp10.upper() == gabarito[9][1]:
        acertos.append(gabarito[9][0])
    else:
        erros.append(gabarito[9][0])
    

    
    i = input("Deseja digitar as notas de outro aluno? Caso deseje sair digite 0: ")