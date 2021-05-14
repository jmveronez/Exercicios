#1.	Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.

n = int(input("Digite o valor desejado para obter a tabuada: "))
for i in range(1,11):
    print("%d x %d = %d"%(n,i,n*i))