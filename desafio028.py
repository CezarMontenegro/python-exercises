#Escreva um programa que faça o computar "pensar" em um número
#inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
#o númeor escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceo ou perdeu

import random

randomNumber = random.randint(0,5)

userNumber = int(input('Digite seu palpite aqui: '))

if randomNumber == userNumber:
    print('Você ganhou meste!')
else:
    print('Você perdeu loser')
