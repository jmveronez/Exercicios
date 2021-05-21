# Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas
# celebridades em um dicionário. Ao escolher uma celebridade, seu programa deve
# retornar a data completa. Não esqueça de validar se a celebridade escolhida está
# presente em seu dicionário.

aniversario = dict()

while True:
    nome = input("Digite o nome da celebridade ou 0 para sair: ")
    if nome == "0": break
    data = input("Digite a data de nascimento da celebridade (dd/mm/yyyy): ")
    sexo = input("Digite o sexo da celebridade: ")
    aniversario[nome] = [data, sexo]

for k,v in aniversario.items():
    print(f"{k}\t - \t {v[0]}\t-\t{v[1]}")

for item,valor in aniversario.items():
    print(f"{item} - {valor}")

print()
nome = input("Digite o nome a ser pesquisado para obter a data de nascimento associada: ")
print(aniversario.get(nome,"Nome não encontrado!"))