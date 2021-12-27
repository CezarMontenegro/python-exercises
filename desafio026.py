#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a útima vez.

frase = str(input('Digite sua frase aqui: ')).upper()

countFrase = frase.count('A')
findFrase = frase.find('A')
rFindFrase = frase.rfind('A')

print(countFrase, findFrase, rFindFrase)