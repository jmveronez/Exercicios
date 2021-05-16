#- Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
#Os códigos utilizados são:
#•	1 , 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
#•	5 - Voto Nulo
#•	6 - Voto em Branco
#Faça um programa que calcule e mostre:
#•	O total de votos para cada candidato;
#•	O total de votos nulos;
#•	O total de votos em branco;
#•	A percentagem de votos nulos sobre o total de votos;
#•	A percentagem de votos em branco sobre o total de votos.
#  Para finalizar o conjunto de votos tem-se o valor zero.

Canditato1 = []
Canditato2 = []
Canditato3 = []
Nulo = []
Branco = []

def eleicao():
    voto = int
    while voto != 0:
        voto = int(input("\nDigite o valor desejado:\n1 - Candidato Gonzaga\n2 - Candidatata Neusa\n3 - Candidato Nilton\n4 - Nulo\n5- Branco\n"))
        if voto == 1:
            Canditato1.append(voto)
        if voto == 2:
            Canditato2.append(voto)
        if voto == 3:
            Canditato3.append(voto)
        if voto == 4:
            Nulo.append(voto)
        if voto == 5:
            Branco.append(voto)
        if voto > 5:
            print("Valor inválido, digite novamente!")
            continue
        
    votos_totais = len(Canditato1) + len(Canditato2) + len(Canditato3) + len(Nulo) + len(Branco)
    media_Nulos = (len(Nulo) / votos_totais) * 100
    media_Brancos = (len(Branco) / votos_totais) * 100
    print("O total de votos foi",votos_totais)
    print("\nO candidato Gonzaga recebeu",len(Canditato1),"votos!")
    print("A candidata Neusa recebeu",len(Canditato2),"votos!")
    print("O candidata Nilton recebeu",len(Canditato3),"votos!")
    print("O total de votos nulos foi de",len(Nulo),"!")
    print("O total de votos em branco foi de",len(Branco),"!")
    print("A média de votos Nulos em relação aos votos totais foi de {0:.2f} %".format(media_Nulos))
    print("A média de votos Brancos em relação aos votos totais foi de {0:.2f} %".format(media_Brancos))

eleicao()
