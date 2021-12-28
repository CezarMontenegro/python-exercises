#Desenvolva um programa que leia o comprimento de tres retas e diga
#ao usuário se elas podem ou náo formar um triangulo.

r1 = float(input('Digite reta 1: '))
r2 = float(input('Digite reta 2: '))
r3 = float(input('Digite reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas podem formar um triangulo!')
else:
    print('Essas retas não podem formar um triangulo!')