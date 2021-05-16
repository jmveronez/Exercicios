#Um professor, muito legal, fez 3 provas durante um semestre, 
# mas só vai levar em conta as duas notas mais altas para calcular a média.
#Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, 
# a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.

notas = []
notas.append(int(input("Digite a primeira nota: ")))
notas.append(int(input("Digite a segunda nota: ")))
notas.append(int(input("Digite a terceira nota: ")))

def calcula_media(notas):
    media = sum(notas) / len(notas)
    print("A média de suas notas total foi",media)
    print("A maior nota foi",max(notas))
    print("A menor nota foi",min(notas))
    notas.remove(min(notas))
    media2 = sum(notas) / len(notas)
    print("A média de suas notas final vai ser",media2)

calcula_media(notas)