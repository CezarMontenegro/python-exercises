#Faça um programa que leia 5 valores e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as 
# suas respectivas posições na lista.

valores = []
maior = 0
menor = 1000

for c in range(0,5):
    valores.append(int(input('Digite o valor: ')))
    if valores[c] > maior:
        maior = valores[c]
    if valores[c] < menor:
        menor = valores[c]

print(valores.index(maior))
print(valores.index(menor))
 