#Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os calores 
# pares e os valores ímpares digirados, respectivamenre. 
# Ao final, mostre o conteúdo das três listas geradas.

values = []
even = []
odd = []
test = ''

while test != 'N':
    n = int(input('Digite um Inteiro: '))
    values.append(n)
    test = input('Deseja continar? [S/N]').upper()

for i in values:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(sorted(values))
print(sorted(even))
print(sorted(odd))