#Exercício 1 - Escreva um programa que pede a senha ao usuário,
#  e só sai do looping quando digitarem corretamente a senha.

senha = input("Digite sua senha:\n")

confirmacao = ""

while confirmacao != senha:
    confirmacao = input("Confirme sua senha:\n")
print("Senha correta")