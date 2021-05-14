#4.	Dada uma string com uma frase informada pelo usuário 
#(incluindo espaços em branco), conte quantas vezes aparece uma vogal.

def conta_vogal(frase):
    vogais = 0
    for letra in frase:
        if letra.upper() == "A":
            vogais += 1
        elif letra.upper() == "E":
            vogais += 1
        elif letra.upper() == "I":
            vogais += 1
        elif letra.upper() == "O":
            vogais += 1
        elif letra.upper() == "U":
            vogais += 1
    return vogais

frase_str = input("Digite uma palavra ou frase para contarmos as vogais: ")
print("A palavra/frase",frase_str,"possui",conta_vogal(frase_str),"vogais")