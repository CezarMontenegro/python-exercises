#Faça um programa que ajude um jogador da Mega Sena a criar palpites. 
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

quantidade = int(input('Quantos jogos você quer fazer? '))
jogos = []
jogo = []
c2 = 0

for c in range(0, quantidade):
    while c2 < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            c2 += 1
    jogo.sort()
    print(jogo)
    jogo.clear()
    c2 = 0

    
    
