#4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas
#  ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def pagamento(horas, valor):
    horas_trabalhadas = float(horas)
    valor_horas = float(valor)
    if horas_trabalhadas <= 40:
        salario = horas*valor
    else:
        horas_extras = horas_trabalhadas - 40
        salario = 40*valor_horas+(horas_extras*(1.5*valor_horas))
    return salario

str_horas = int(input("Quantas horas foram trabalhadas no mês? "))
str_taxa = int(input("Qual a taxa de valor por hora trabalhada? "))

salario_total = pagamento(str_horas, str_taxa)
print("Você irá receber R$",salario_total)