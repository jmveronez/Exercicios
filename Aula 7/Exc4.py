#Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o 
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
# tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. 
# Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime


def voto(ano_nascimento):
    if 2021 - ano_nascimento < 16:
        print("VOTO NEGADO")
    if 2021 - ano_nascimento < 18:
        print("VOTO OPCIONAL")
    else:
        print("VOTO OBRIGATÓRIO")

ano_nascimento = int(input("Digite o ano em que nasceu: "))

voto(ano_nascimento)

#Desculpe, não consegui resolver utilizando a biblioteca Datetime pois não a entendi muito bem