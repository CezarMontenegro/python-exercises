#Escreva um programa que leia um valor em metros e o exiba
#convertido em centimetros e milimetros

var = float(input('Digite sua medida em metros aqui:'))

print('Sua medida convertida em centimetros é {:.0f}cm'.format(var * 100))
print('Sua medida convertida em milemetro é {:.0f}mm'.format(var * 1000))