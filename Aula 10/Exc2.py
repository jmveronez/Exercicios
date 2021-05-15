#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando 
# o número do aluno e o segundo representando a sua altura em centímetros.  
# Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do 
# aluno mais baixo, junto com suas alturas.

id_aluno = []
altura = []

while len(id_aluno) < 10:
    id = id_aluno.append(int(input("Digite o número do aluno: ")))
    aaltura = altura.append(int(input("Digite a altura deste aluno em cm: ")))

print("O maior aluno tem",max(altura))
print("O menor aluno tem",min(altura))
