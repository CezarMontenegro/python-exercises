#Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar. 
# No final, mostre: 
# A) Qual é o total gasto na compra. 
# B) Quantos produtos custam mais de R$1000. 
# C) Qual é o nome do produto mais barato.

total = 0
maisDeMil = 0
maisBarato = 0
menor = 1000
contador = 0

teste = ''

while teste != 'N':
    name = input('Digite o nome do produto: ')
    price = int(input('Digite o preço do produto: '))

    total += price
    if price >= 1000:
        contador += 1
    if price < menor:
        menor = price
        maisBarato = name
    
    teste = input('Deseja Continuar? [S/N]').upper()

print(f'O total gasto foi {total}')
print(f'{contador} produtos custam mais de R$ 1000 reais')
print(f'O produto mais barato é {maisBarato}')
