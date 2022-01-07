#Faça um programa que leia nome e média de um aluno, guardando também 
# a situação em um dicionário. No final, mostre o centeúdo da estrutura 
# na tela.

dicionario = { }

dicionario['nome'] = str(input('Digite o nome: '))
dicionario['media'] = float(input('Digite a média: '))

if dicionario['media'] < 7:
    print(f'O aluno {dicionario["nome"]} está reprovado :(')
elif dicionario['media'] >= 7:
    print(f'O aluno {dicionario["media"]} está aprovado :)')

