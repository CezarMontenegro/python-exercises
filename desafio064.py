#Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final mostre quantos números 
# foram digitados e qual foi a soma entre eles

n = 0
contador = 0
somatorio = 0

while n != 999:
    n = int(input('Digite o inteiro: '))
    if n != 999:
        contador += 1
        somatorio += n
print('Forma digitados {} números e o somatorio foi {}'.format(contador, somatorio))
 