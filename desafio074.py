#Crie um programa que vai gerar cinco números aleatórios e colocar
#em uma tupla. Depois disso, mostre a listagem de números gerados 
#e também indique o menor e o maior valor que estão na tupla.

from random import randint

inteiros = (randint(1,1000), randint(1,1000), randint(1,1000),
    randint(1,1000), randint(1,1000))
menor = 1001
maior = 0

for inteiro in inteiros:
    if inteiro > maior:
        maior = inteiro
    
    if inteiro < menor:
        menor = inteiro

print(inteiros)
print(maior)
print(menor)

