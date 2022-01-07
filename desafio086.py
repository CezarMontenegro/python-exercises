#Crie um programa que crie uma matriz de mimensão 3x3 e preencha com valores lidos 
# pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matrix = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input('Digite um valor: '))

for l in range(0,3):
    for c in range(0,3):
        print(matrix[l][c], end='')
    print()