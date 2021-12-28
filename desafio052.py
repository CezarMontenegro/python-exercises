#Faça um programa que leia um número inteiro e diga se ele é um número primo

n = int(input('Digite um inteiro: '))
somatorio = 0

for c in range(2, n):
    if n % c == 0:
        somatorio +=1

if somatorio != 0:
    print('O número {} não é primo'.format(n))
else:
    print('O número {} é primo'.format(n))