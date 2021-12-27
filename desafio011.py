#Faça um programa que leia a largura e a altura de uma parede em metros
#e calcule sua área e a quantidade de tinta necessário para pinta-la
#sabendo que cada litro de tinta rende 2m2

altura = float(input('Digite altura aqui:'))
largura = float(input('Digite largura aqui:'))

rendimento = (largura * altura) / 2

print('Você irá precisar de  {}L '.format(rendimento))