#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. Valide a data e retorne NULL 
# caso a data seja inválida.

def Escreve_Data(dia,mes,ano):
    if dia > 0 and dia <= 31 and ano > 0:
        if mes == 1:
            print(dia,"de Janeiro de",ano)
        elif mes == 2:
            print(dia,"de Fevereiro de",ano)
        elif mes == 3:
            print(dia,"de Março de",ano)
        elif mes == 4:
            print(dia,"de Abril de",ano)
        elif mes == 5:
            print(dia,"de Maio de",ano)
        elif mes == 6:
            print(dia,"de Junho de",ano)
        elif mes == 7:
            print(dia,"de Julho de",ano)
        elif mes == 8:
            print(dia,"de Agosto de",ano)
        elif mes == 9:
            print(dia,"de Setembro de",ano)
        elif mes == 10:
            print(dia,"de Outubro de",ano)
        elif mes == 11:
            print(dia,"de Novembro de",ano)
        elif mes == 12:
            print(dia,"de Dezembro de",ano)
        else:
            print("NULL")
    else:
        print("NULL")

str_dia = int(input("Digite o dia: "))
str_mes = int(input("Digite o mês: "))
str_ano = int(input("Digite o ano: "))

Escreve_Data(str_dia,str_mes,str_ano)