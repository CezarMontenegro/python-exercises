#Faça um programa que leia o nome completo de uma pessoa, mostrando
#em seguida o primeiro e o último nome separadamente.

name = input('Digite seu nome aqui: ')

name = name.split()
firstName = name[0]
lastName = name[len(name) - 1]

print('Primeiro = {}'.format(firstName))
print('Último = {}'.format(lastName))