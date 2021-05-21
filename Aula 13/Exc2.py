# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feito em cada partida. No final tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
partidas = []
jogador['nome'] = input("Digite o nome do jogador: ")
total = int(input("Digite o total de partidas jogadas: "))
for i in range(total):
    partidas.append(int(input(f"Digite a quantidade de gols na partida {i+1}: ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print("*-=-*"*30)
print("Nome do Jogador: ", jogador['nome'])
print("*-=-*"*10)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
print("*-=-*"*10)
for k,v in enumerate(jogador['gols']):
    print(f" - Na partida {k+1}, ele fez {v} gols!")
print("*-=-*")
print(f"O jogador {jogador['nome']} fez um total de {jogador['total']} gols no campeonato.")