#Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6,
#7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes
#aos quadrados desses números.

lista_numeros1 = [1,4,5,6,7,9]
Numeros1 = {i:i**2 for i in lista_numeros1}
print(Numeros1)

lista_numeros = [(1,1**2),(4,4**2),(5,5**2),(6,6**2),(7,7**2),(9,9**2)]
Numeros = dict(lista_numeros)
print(Numeros)