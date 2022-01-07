#Crie um programa onde 4 hogadores joguem um dado e tenham resultados
#aleatórios. Guarde esses resultados em um dicionário. No final, 
#coloque esse dicionário em ordem, sabendo que o vencedor tirou o 
#maior número no dado.

from random import randint
from operator import itemgetter

dicionario = {}
ranking = {}

for c in range(1, 5):
    dicionario[f'Jogador {c}'] = randint(1,6)

ranking = sorted(dicionario.items(), key=itemgetter(1), reverse = True)

print(ranking)