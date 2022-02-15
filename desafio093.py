#Crie um programa que gerencie o aproveitamento 
# de um jogador de futebol. O programa vai ler o
#  nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em 
# cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols 
# feitos durante o campeonato.

dicionario = {}
gols = []

dicionario['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Quantas partidas o jogador jogou? '))

for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))

dicionario['gols'] = gols
dicionario['total'] = sum(gols)

print('-=' * 30)
print(dicionario)
print('-=' * 30)

for c in range(1, partidas + 1):
    print(f'  => Na partida {c}, fez {gols[c - 1]} gols.')
print(f'Foi um total de {dicionario["total"]} gols.')
