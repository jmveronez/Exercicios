#Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas 
# expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
# A função “altera” 1o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    Novo_Preco = custo * (1 + (taxaImposto / 100))
    return Novo_Preco

custo = int(input("Digite o valor de um produto: "))
taxaImposto = float(input("Digite a porcentagem do imposto que será aplicado: ").replace(',','.'))

print("O valor original é:",custo,",e seu novo preço passará a ser:",somaImposto(taxaImposto,custo))