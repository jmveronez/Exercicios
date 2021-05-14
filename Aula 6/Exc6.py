#6.	Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).

def definir_nota(nota):
    if nota >= 9.0 and nota <= 10:
        print("A")
    elif nota >= 8.0 and nota < 9:
        print("B")
    elif nota >= 7.0 and nota < 8:
        print("C")
    elif nota >= 6.0 and nota < 7:
        print("D")
    elif nota >= 5.0 and nota < 6:
        print("E")
    elif nota < 5 and nota >= 0:
        print("F")
    else:
        print("Digite um valor válido")

float_nota = float(input("Digite o valor do aluno: ").replace(",","."))

definir_nota(float_nota)