#Desenvolva um programa que pergunte a distancia de uma viagem em Km.
#Calcule o preço da passagem . Cobrando R$ 0,50 por Km para viagens
#de até 200Km e R$0,45 para viagens mais longas.

dist = int(input('Qual a distancia da viagem em Km? '))

if dist <= 200:
    print('O preço da passagem é R${}'.format(dist * 0.50))
else:
    print('O preço da passagem é R${}'.format(dist*0.45))