#Crie um programa que leia o nome de uma cidade e diga se ela
#começa com a palavra "SANTO"

name = input('Digite o nome da sua cidade aqui: ')

firstName = name.split()[0].upper()

print(firstName == 'SANTO')