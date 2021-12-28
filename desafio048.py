#Faça um programa que calcule a soma entre todos os números impares
#  que são múltiplos de três e que se encontram no intervalo 
# de 1 á 500.

somatorio = 0

for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        somatorio += c
print(somatorio)