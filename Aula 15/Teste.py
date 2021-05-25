class pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def mostrar_dados(self):
        print(f"Olá, meu nome é {self.nome} {self.sobrenome} e tenho {self.idade} anos")

str_nome = input("Digite seu nome: ")
str_sobrenome = input("Digite seu sobrenome: ")
int_idade = int(input("Digite sua idade: "))

pessoa1 = pessoa(str_nome,str_sobrenome,int_idade)
pessoa1.mostrar_dados()