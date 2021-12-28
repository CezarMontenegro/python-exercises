#Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
#No final do programa. mostre: 
#-A média de idade do grupo. 
#-Qual é o nome do homem mais velho. 
#-Qauntas mulheres têm menos de 20 anos.

media = 0
maiorIdade = 0
maisVelho = ''
contador = 0

for c in range(1, 5):
    n = input('Digite seu nome: ')
    i = int(input('Digite sua idade: '))
    s = input('Digite seu sexo: ')

    media += i

    if s == 'm':
        if i > maiorIdade:
            maiorIdade = i
            maisVelho = n

    if s == 'f':
        if i < 20:
            contador += 1
        
print('A média de idade é {}'.format(media / 4))
print('O homem mais velho é {}'.format(maisVelho))
print('{} mulheres tem menos de 20 anos'.format(contador))


