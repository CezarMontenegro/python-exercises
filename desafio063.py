#Escreva um programa que leia um número n inteiro qualquer e 
#mostre na tela os n primeiros elementos de uma sequencia de
#fibonacci.

n = int(input('Digite quantos termos você quer mostrar: '))
a = 1
b = 1
c = a + b
contador = 4
 
print(0)
print(1)
print(1)
print(2)

while contador < n:
    a = b
    b = c
    c = a + b
    print(c)
    contador += 1