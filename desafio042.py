#Desenvolva um programa que leia o comprimento de tres retas e diga
#ao usuário se elas podem ou náo formar um triangulo.
#Diga que tipo de triangulo será formado: 
# -Equilatero: todos os lados iguais 
# -Isoceles: dois lados iguais 
# -Escaleno: todos os lados diferentes

r1 = float(input('Digite reta 1: '))
r2 = float(input('Digite reta 2: '))
r3 = float(input('Digite reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Equilátero: todos os lados iguais')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Isóceles: dois lados iguais')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Escaleno: todos os lados diferentes')
else:
    print('Não e possível formar um triangulo com essas retas')