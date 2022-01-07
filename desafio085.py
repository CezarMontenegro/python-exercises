#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em 
# uma lista única que mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

list = [[],[]]

for c in range(0,7):
    n1 = int(input('Digite um inteiro: '))
    if n1 % 2 == 0:
        list[0].append(n1)
    else:
        list[1].append(n1)
print(f'Pares = {list[0]}')
print(f'Ímpares = {list[1]}')