#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário
#  e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas 
# da frase original.

def vogais(frase):
    vogais = 0
    vogais_1 = "AEIOUÁÀÃÂÉÈÊÓÒÔÕÚÙÛÍÌÎ"
    palavra_alterada = frase
    for letra in frase:
        if letra.upper() in vogais_1:
            vogais += 1

    for letra in palavra_alterada:
        if letra.upper() in vogais_1:
            palavra_alterada = palavra_alterada.replace(letra,"")
    print(f"A frase ou palavra {frase} possui {vogais} vogais e fica {palavra_alterada} sem elas")

frase = input("Digite uma frase ou palavra e veja a mágica acontecer: ")

vogais(frase)