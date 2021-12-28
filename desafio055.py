#Faça um programa que leia o peso de cinco pessoas. No final, 
#mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 1000

for c in range(1,6):
    n = float(input('Digite o peso em kg aqui: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n

print('O menor peso é {}'.format(menor))
print('O maior peso é {}'.format(maior))