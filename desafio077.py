#Crie um programa que tenha uma tupla com várias palavras
#(não usar acentos). Depois disso, você deve mostrar, para cada 
#palavra, quais são as suas vogais.

palavras = ('caderno', 'mesa', 'cadeira', 'cama', 'mesa', 'cachorro')

for palavra in palavras:
    print('\n')
    for letra in palavra:
        if letra in 'aeiou':
          print(letra, end = ' ')
