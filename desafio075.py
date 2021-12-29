#Desenvolva um programa que leia quatro valores pelo teclado e 
# guarde-os em uma tupla. No final, mostre: 
# A)Qquantas vezes apareceu o valor 9. 
# B)Em que posição foi digitado o primeiro valor 3. 
# C)Quais foram os números pares.

valores = (
   int(input('Digite o valor: ')),
   int(input('Digite o valor: ')),
   int(input('Digite o valor: ')),
   int(input('Digite o valor: ')),
)

print(valores.count(9))
print(valores.index(3))

for valor in valores:
    if valor % 2 == 0:
        print(valor, end = ' ')