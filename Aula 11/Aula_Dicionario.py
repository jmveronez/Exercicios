Vingadores_lista = [("Chris Evans","Capitão América"),("Mark Ruffalo","Hulk"),("Tom Hiddleston","Loki"),("Chris Hemworth","Thor"),("Robert Downey Jr","Homem de Ferro"),("Scarlett Johansson","Viúva Negra")]
Vingadores = dict(Vingadores_lista)
ator = input("Digite o ator para pesquisarmos seu personagem: ")
print(Vingadores.get(ator,"Ator não encontrado"))