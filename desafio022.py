#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome

name = input('Digite seu nome completo aqui: ')

upperName = name.upper()
lowerName = name.lower()
countName = len(name)
firstName = len(name.split()[0])


print(upperName)
print(lowerName)
print(countName)
print(firstName)


