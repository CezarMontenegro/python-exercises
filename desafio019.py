#Um professor quer sortear um dos seus quatro alunos para apagar
#o quadro. Faça um programa que ajude ele, lendo o nodeles e
#escrevendo o nome do escolhido

import random

n1 = input('Digite nome do aluno: ')
n2 = input('Digite nome do aluno: ')
n3 = input('Digite nome do aluno: ')
n4 = input('Digite nome do aluno: ')

list = [n1, n2, n3, n4]

escolhido = random.choice(list)

print('O aluno escolhido foi {}'.format(escolhido))