#Faça um programa que leia um ano qualquer e mostre se ele é bissesto

ano = int(input('Digite o ano aqui: '))

if ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é bissesto'.format(ano))
else:
    print('O ano {} não é bissesto'.format(ano))