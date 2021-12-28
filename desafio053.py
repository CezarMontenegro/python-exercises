#Crie um programa que leia uma frase e diga se ela é um palíndromo 
#desconsiderando os espaços

frase = input('Digite sua frase aqui: ')
frase = frase.split()
frase = ''.join(frase)

n = len(frase)

contrario = ''

for c in range(n -1, -1, -1):
    contrario += frase[c]

if contrario == frase:
    print('Sua frase é um palíndromo')
else:
    print('Sua frase não é um palíndromo')
