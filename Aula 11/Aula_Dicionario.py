Vingadores_lista = [("Chris Evans","Capitão América"),("Mark Ruffalo","Hulk"),("Tom Hiddleston","Loki"),("Chris Hemworth","Thor"),("Robert Downey Jr","Homem de Ferro"),("Scarlett Johansson","Viúva Negra")]
Vingadores = dict(Vingadores_lista)
Vingadores['Arnaldo e suas nega'] = 'Exterminador do futuro'
Vingadores['Silvester está sozinho'] = 'Rambo'
Vingadores['Joaquin Phoenix'] = 'Coringa'
Vingadores['Tobey Macguire'] = 'Miranha'
Vingadores['Jason Momoa'] = 'Um estranho no ninho'
print(Vingadores)
ator = input("Digite o ator para pesquisarmos seu personagem: ")
print(Vingadores.get(ator,"Ator não encontrado"))
Vingadores.pop('Silvester está sozinho')
print(Vingadores)

Vilões = {"CGI":"Thanos","Cavera":"Vermelha","Miranha":"Negro do Espaço"}

for item in Vilões:
    print(item)
    Vingadores[item] = Vilões[item]
    input()

print(Vingadores)