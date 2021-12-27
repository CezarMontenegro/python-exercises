#Faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input('Digite o ângulo aqui: '))

angSin = math.sin(math.radians(ang))
angCos = math.cos(math.radians(ang))
angTan = math.tan(math.radians(ang))

print('O seno é {}, o cosseno é {} e a tangente é {}'
    .format(angSin, angCos, angTan))