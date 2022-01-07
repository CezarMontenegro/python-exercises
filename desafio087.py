#Crie um programa que crie uma matriz de mimensão 3x3 e preencha com valores lidos 
# pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
#A)Some todos os valores pares digitados
#B)A soma dos valores da terceira coluna.
#)O maior valor da segunda linha.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even = []
sumThird = 0
sumLine = 0

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input('Digite um valor: '))
        if matrix[l][c] % 2 == 0:
            even.append(matrix[l][c])

for l in range(0, 3):
    sumThird += matrix[l][2]

for c in range(0, 3):
    sumLine += matrix[1][c]

print(even)
print(sumThird)
print(sumLine)