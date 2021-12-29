#Crie um programa que simule o funcionamento de um caixa eletroncio. 
#No início, pergunte ao usuário qual será o valor a ser sacado 
#(número inteiro) 
#e o programa vai informar quantas cédulas de 
#cada valor serão entregues. obs. Considere que o caixa possui 
#cédulas de R$50, R$20, R$10, R$1.

valor = int(input('Digite o valor a ser sacado: '))

cinquenta = valor // 50
vinte = (valor % 50) // 20
dez = (valor % 50 % 20) // 10
cinco = (valor % 50 % 20 % 10) // 5
um = (valor % 50 % 20 % 10 % 5) // 1

print(f'50 - {cinquenta} cédulas')
print(f'20 - {vinte} cédulas')
print(f'10 - {dez} cédulas')
print(f'05 - {cinco} cédulas')
print(f'01 - {um} cédulas')
