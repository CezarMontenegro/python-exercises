#Desenvolva um programa que leia seis números inteiros e mostre 
# a soma apenas daqueles que foem pares. Se o valor digitado for 
# impar, desconsidere-o

somatorio = 0

for c in range(1,7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        somatorio += n
print(somatorio)