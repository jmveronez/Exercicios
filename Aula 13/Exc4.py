# Uma escola te contratou para desenvolver um programa em Python para que o
# professor gerencie as notas de seus alunos. Seu programa deve apresentar o seguinte
# menu:
# 0. Sair
# 1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
# 2. Inserir aluno e nota
# 3. Alterar a nota de um aluno
# 4. Consultar nota de um aluno específico
# 5. Apagar um aluno da lista
# 6. Exibir a média da turma
# As notas e os nomes dos alunos serão fornecidos pelo professor. Implemente a sua
# solução utilizando dicionário.

def menu():
    while True:
        print("*-=-*"*10)
        print("Escola da tia Teteia")
        print("*-=-*")
        print("\t 0. Sair")
        print("\t 1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)")
        print("\t 2. Inserir aluno e nota")
        print("\t 3. Alterar a nota de um aluno")
        print("\t 4. Consultar nota de um aluno específico")
        print("\t 5. Apagar um aluno da lista")
        print("\t 6. Exibir a média da turma")
        print("*-=-*"*10)
        op = input("Digite a opção desejada: ")
        if op == '0':
            break
        elif op == '1':
            exibir()
        elif op == '2':
            inserir()
        elif op == '3':
            alterar()
        elif op == '4':
            consultar()
        elif op == '5':
            apagar()
        elif op == '6':
            exibir_media()
        else:
            print("Opção Inválida! Tente Novamente!")

def exibir():
    if len(alunos) > 0:
        for aluno in alunos:
            print("\tNome: {aluno}\t-\tNota: {alunos[aluno]}")
    else:
        print("\tLISTA DE ALUNOS VAZIA!")

def inserir():
    aluno = input("\tDigite o nome do aluno: ")
    nota = float(input("\tDigite a nota do aluno: "))
    if alunos.get(aluno):
        print("Aluno já consta na lista. Caso deseje alterar a nota, selecione a opção correta.")
    else:
        alunos.update({aluno:nota})
        print(f"\tAluno {aluno} inserido com sucesso!")

def alterar():
    aluno = input("\tDigite o nome do aluno: ")
    nota = float(input("\tDigite a nota do aluno: "))
    if (aluno not in alunos):
        print("Aluno não consta na lista. Caso deseje inserir a nota, selecione a opção correta.")
    else:
        alunos.update({aluno:nota})
        print(f"\tAluno {aluno} alterado com sucesso!")

def consultar():
    aluno = input("\tDigite o nome do aluno: ")
    if (aluno not in alunos):
        print("Aluno não consta na lista. Caso deseje inserir a nota, selecione a opção correta.")
    else:
        print("\tNome: {aluno}\t-\tNota: {alunos[aluno]}")

def apagar():
    aluno = input("\tDigite o nome do aluno: ")
    if (aluno not in alunos):
        print("Aluno não consta na lista. Caso deseje inserir a nota, selecione a opção correta.")
    else:
        alunos.pop(aluno)
        print(f"\tAluno {aluno} apagado com sucesso!")

def exibir_media():
    soma = 0
    for nota in alunos.values():
        soma += nota
    if len(alunos) > 0:
        media = soma / len(alunos)
    else:
        media = 0.0
    print(f"\t A média da turma é {media:.2f}!")


alunos = dict()
menu()