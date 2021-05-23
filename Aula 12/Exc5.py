# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade
# , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve
# contribuir por 35 anos para se aposentar.

import datetime

dados_funcionario = {}

parada = True

while parada != "sair":
    nome = input("Digite o nome do funcionário: ")
    data_nasc = input("Digite o ano de nascimento (DD/MM/YY): ")
    dt = datetime.datetime.strptime(data_nasc, "%d %m %y")
    ctps = input("Digite o número da carteira de trabalho: ")
    idade = datetime.datetime.now().year - dt.year
    dados_funcionario.update({'nome': nome, 'data de nascimento': data_nasc,'idade':idade})
    if ctps != '0':
        data_contrat = input("Digite o ano de contratação (DD/MM/YY): ")
        dt = datetime.datetime.strptime(data_contrat, "%d/%m%y")
        aposentadoria = dt.year + 35 - idade
        salario = input("Digite o salário: ")
        dados_funcionario.update({'ano da contratação':data_contrat,'salário':salario,'previsão de aposentadoria':aposentadoria})
        
    parada = input("Digite enter para outr funcionario ou digite sair para encerrar:").lower()
print(dados_funcionario)