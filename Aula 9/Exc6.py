#6.	Faça um script que peça ao usuário o número de matérias da escola, ou seja, um inteiro positivo. 
# Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso será armazenado numa lista. 
# Ao final, seu script deverá fornecer a média geral do aluno.

n = int(input("Quantas matérias serão analisadas? "))

notas = []
for i in range(n):
    nota = float(input("Digite a nota da matéria: "))
    notas.append(nota)

media = sum(notas)/len(notas)
print("A sua média final é:",str(media))