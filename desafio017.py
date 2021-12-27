#Faça um programa que leia o comprimento do cateto oposto
#do cateto adjascente de um triangulo retangulo e mostre
#o comprimento da hipotenusa

from math import sqrt

co = float(input('Digite aqui o cateto oposto: '))
ca = float(input('Digite aqui o cateto adjascente: '))

hip = sqrt((co ** 2) + (ca ** 2))

print('A hipotenusa é {}'.format(hip))