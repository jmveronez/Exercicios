#08 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
#  em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de
#  contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai
#  se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from datetime import date, datetime

dados = dict()

dados['Nome'] = input("Digite o nome do colaborador: ")
nasc = int(input("Digite o seu ano de nascimento: "))
if nasc > 0:
    dados['Idade'] = datetime.now().year - nasc
    dados['CTPS'] = int(input("Digite o número de sua carteira de trabalho, caso não tenha digite 0: "))
    if dados['CTPS'] != 0:
        dados['Contratacao'] = int(input("Digite o ano em que foi contratado: "))
        if dados['Contratacao'] < nasc:
            print("Digite uma data válida!")
            dados['Contratacao'] = None
        else:
            dados['Salario'] = float(input("Digite o valor do seu último salário: R$"))
            dados['Aposentadoria'] = (dados['Contratacao'] - nasc) + 35
            print("-=-"*30)
            for k, v in dados.items():
                print(f"\n{k}: {v}")
                break
    for k, v in dados.items():
            print(f"\n{k}: {v}")
else:
    print("Valor Inválido!")
    nasc = int(input("Digite o seu ano de nascimento: "))