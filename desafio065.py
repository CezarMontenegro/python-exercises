#Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e 
# qual foi o maior e o menor valor lidos. O programa deve perguntar 
# ao usuário se ele quer ou não coninuar a digitar valores.

test = ''
somatorio = 0
maior = 0
menor = 100000
c = 0
while test != 'N':
    n = float(input('Digite o valor aqui: '))
    somatorio += n
    c += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    test = input('Deseja continuar? [S/N]').upper()
print('A média foi {}'.format(somatorio / c))
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))