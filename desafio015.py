# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa 
# R$60 por dia e R$0.15 por ks rodado.

kmRodados = float(input('Digite a quantos Km aqui:'))
diasAlugados = int(input('Digite quantidade de dias alugados aqui:'))

total = (diasAlugados * 60) + (kmRodados * 0.15)

print('O valor total é R${}'.format(total))