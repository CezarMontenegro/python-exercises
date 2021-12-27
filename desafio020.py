#O mesmo professor do desafio anterior quer sortear a ordem de
#apresentação de trabalhos dos alunos. Faça um programa que leia o
#nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = input('Digite nome do aluno: ')
n2 = input('Digite nome do aluno: ')
n3 = input('Digite nome do aluno: ')
n4 = input('Digite nome do aluno: ')

list = [n1, n2, n3, n4]

random.shuffle(list)

print(list)

