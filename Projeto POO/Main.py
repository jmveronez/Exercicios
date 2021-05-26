# Proposta de projeto de ficção interativa para avaliação de OO
# Sugestão: completar com classes filhas colocando pessoas saudáveis, trabalhos menos remunerados, casas melhor equipadas et cetera

import random

class Relogio:
    def __init__(self):
        self.horas = 6
        self.minutos = 0
    
    def __str__(self):
        return (f"|{self.horas:02d}:{self.minutos:02d}|")
    
    def avancaTempo(self, minutos):
        self.minutos += minutos
        while(self.minutos >= 60):
            self.minutos -= 60
            self.horas += 1
    
    def atrasado(self):
        return (self.horas > 7 or (self.horas == 7 and self.minutos > 0))


class Personagem:
    def __init__(self):
        self.sujo = True
        self.fome = True
        self.medicado = False
        self.dinheiro = 0
        self.salario = 100
    
    def __str__(self):
        return "Você está " + ("sujo" if self.sujo else "limpo")+", "+("com" if self.fome else "sem")+" fome e "+("" if self.medicado else "não ")+"tomou sua medicação. Você tem "+str(self.dinheiro)+" reais na sua conta."

    def dormir(self):
        self.sujo = True
        self.fome = True
        self.medicado = False

    def montar_personagem(self):
        self.genero = input("Para começar, você é Homem, Mulher ou outro? ")
        self.idade = int(input("Ótimo, e qual sua idade? "))
        self.nome = input("Bacana, e qual o seu nome? ")
        self.cor = input("E sua cor, por gentileza: ")
        self.altura = float(input("Qual sua altura? ").replace(',','.'))
        self.peso = input("Você gostaria de ser gordo ou magro? ")
        self.cabelo = input("Qual o estilo do seu cabelo? ")
        if self.cabelo.upper() == "CARECA":
            print("KKKKKKKKKKKKKKKKKKK OLHA AÍ A CABECINHA DE GUIDÃO!")
        else:
            self.cor_cabelo = input("E a cor dele? ")
        self.rosto = input("Você é feio ou bonito? ")


class Casa:
    def __init__(self):
        self.remedios = 1
        self.comida = 5

class Eventos:
    def menu_bomdia_atrasado(self):
        print("Bom dia o escambau, levanta e corre para não perder o emprego!")
        print("Ações:")
        print("1 - Correr para o trabalho")
        print("2 - Tomar banho")
        print("3 - Tomar café da manhã")
        print("4 - Tomar remédio")
        print("0 - Sair do jogo!")

    def menu_bomdia_seguro(self):
        print("Bom dia flor do dia, vamos levantar e iniciar um novo dia!")
        print("Ações:")
        print("1 - Ir para o trabalho")
        print("2 - Tomar banho")
        print("3 - Tomar café da manhã")
        print("4 - Tomar remédio")
        print("0 - Sair do jogo!")

    def menu_bomdia_padrao(self):
        print("Ações:")
        print("1 - Acordar")
        print("2 - Dormir mais 5 minutinhos")
        print("0 - Sair do jogo!")

if(__name__ == "__main__"):
    dia = 1
    relogio = Relogio()
    personagem = Personagem()
    casa = Casa
    eventos = Eventos()
    cafe_da_manha = False
    print("---")
    personagem.montar_personagem()
    print("Olá "+str(personagem.nome)+" são "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até às 07:00.")
    eventos.menu_bomdia_padrao()
    opcao = input("Escolha sua ação: ")
    while relogio.horas != 7:
        sorte_sono = random.randint(1,12)
        if(opcao == "1"):
            break
        elif(opcao == "2"):
            if(sorte_sono <= 8):
                print("Ok, durma mais um pouco...")
                relogio.avancaTempo(5)
                eventos.menu_bomdia_padrao()
                opcao = input("Escolha sua ação: ")
            else:
                print("Você dormiu mais do que o necessário e agora está atrasadíssimo!")
                relogio.avancaTempo(45)
                break
        elif(opcao == "0"):
            break
        else:
            print("Opção inválida!")
            continue
    if relogio.atrasado == True:
        print(str(personagem.nome)+" são "+str(relogio)+" do dia "+str(dia)+". Você tinha que sair pro trabalho até as 07:00.")
        eventos.menu_bomdia_atrasado()
        opcao = input("Escolha sua ação: ")
    else:
        print(str(personagem.nome)+" são "+str(relogio)+" do dia "+str(dia)+". Você tem que sair pro trabalho até as 07:00 então cuidado para não atrasar.")
        eventos.menu_bomdia_seguro()
        opcao = input("Escolha sua ação: ")

        # elif(opcao == "3"):
        #     if(personagem.dinheiro >= 15):
        #         personagem.dinheiro -= 15
        #         cafe_da_manha = True
        #     else:
        #         print("O café da manhã custa 15 reais, você não tem dinheiro suficiente.")
        #     relogio.avancaTempo(5)
        # elif(opcao == "4"):
        #     if(cafe_da_manha):
        #         personagem.fome = False
        #         cafe_da_manha = False
        #         relogio.avancaTempo(15)
        #     else:
        #         print("Não tem café da manhã na sua casa.")
        #         relogio.avancaTempo(5)
        # elif(opcao == "5"):
        #     if(casa.remedios > 0):
        #         casa.remedios -= 1
        #         personagem.medicado = True
        #     else:
        #         print("Não tem remédio na sua casa")
        #     relogio.avancaTempo(5)
        # elif(opcao == "6"):
        #     if(personagem.dinheiro >= 20):
        #         casa.remedios += 10
        #         personagem.dinheiro -= 20
        #         relogio.avancaTempo(10)
        #     else:
        #         print("A cartela com 10 remédios custa 20 reais, você não tem dinheiro suficiente.")
        #         relogio.avancaTempo(5)
        # elif(opcao == "7"):
        #     print("-=-=-")
        #     print("Você foi trabalhar.")
        #     print(personagem)
        #     print("-=-=-")
        #     recebido = personagem.salario
        #     if(not personagem.medicado):
        #         print("Como você não tomou seu remédio, você ficou doente no caminho e não chegou no trabalho")
        #         recebido = 0
        #     elif(personagem.sujo):
        #         print("Como você estava sujo, seus colegas reclamaram para seu chefe, e você levou uma advertência.")
        #         recebido *= 0.9
        #     elif(personagem.fome):
        #         print("Como você estava com fome, você trabalhou metade do que consegue trabalhar.")
        #         recebido *= 0.5
        #     elif(relogio.atrasado()):
        #         print("Como você chegou atrasado, você produziu menos do que de costume.")
        #         recebido *= 0.8
        #     print("Você recebeu "+str(recebido)+" reais pelo seu trabalho hoje.")
        #     print("-=-=-")

        #     personagem.dinheiro += recebido
        #     personagem.dormir()
        #     relogio = Relogio()
        #     dia+=1