#5.	O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 
# e agora possui uma loja de conveniências. Faça um programa que implemente uma 
# caixa registradora rudimentar. O programa deverá receber um número desconhecido 
# de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador 
# para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor
#  em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
# Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. 
# A saída deve ser conforme o exemplo abaixo


produtos = []
produto = int
while produto != 0:
    produto = float(input("Digite o valor dos produtos comprados, digite 0 para sair: "))
    if produto > 0:
        produtos.append(produto)
    else:
        break

def caixa_registradora(produtos):
    valor_total = sum(produtos)
    print("\nO valor total da compra é R$",valor_total,"\n")
    dinheiro = float(input("Quanto o cliente está pagando? "))
    troco = dinheiro - valor_total
    if troco > 0:
        print("O troco será de R$",troco)
    else:
        print("Não precisa de troco.")

caixa_registradora(produtos)