#Faça um programa que leia um número qualquer e mostre 
#o seu fatorial.

num = int(input('Digite um número: '))
fatorial = 1
c = 1

# for c in range(1, num + 1):
#     fatorial *= c
# print(fatorial)

while c < num:
    c += 1
    fatorial *= c
print(fatorial)