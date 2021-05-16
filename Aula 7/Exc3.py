#Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
#  Faça uma chamada à função, passando como parâmetro uma string.

def MAIUSCULANDO(frase):
    return frase.upper()

str_frase = input("Digite uma palavra ou frase: ")

print(MAIUSCULANDO(str_frase))