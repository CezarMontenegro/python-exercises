#Crie um programa que leia nome e duas notas de vários alunos e 
# guarde tudo em um alista composta. No final, mostre um boletim 
# contendo a média de cada um e permita que o usuário possa mostrar 
# as notas de cada aluno individualmente.

test = 'A'
ficha = []

while test != 'N':
    nome = str(input('Digite o nome: '))
    n1 = float(input('Digite n1: '))
    n2 = float(input('Digite n2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    test = str(input('Deseja continuar? [S/N]')).upper()


print(ficha)
        