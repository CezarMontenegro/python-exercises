#Crie um programa que leia um número Real qualquer pelo teclado
#e mostre na tela a sua porção Inteira

from math import trunc

var = float(input('Digite um numero decimal: '))

print(trunc(var))