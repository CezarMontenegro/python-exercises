#Faça um programa que leia nome e peso de várias pessoas guardando tudo em uma lista.
# No final, mostre: 
# A)Quantas pessoas foram cadastradas.
# B)Uma listagem com as pessoas mais pesadas.
# C)Uma listagem com as pessoas mais leves.

list = []
data = []
test = ''
fatter = []
thinner = []
higherWeight = 0
lowerWeight = 1000

while test != 'N':
    data.append(str(input('Digite o nome: ')))
    data.append(int(input('Digite o peso:')))
    list.append(data[:])
    data.clear()
    test = str(input('Deseja continuar? [S/N]')).upper()

for c in list:
    if c[1] > higherWeight:
        higherWeight = c[1]
        fatter.clear()
        fatter.append(c[0])
    elif c[1] == higherWeight:
        fatter.append(c[0])
    elif c[1] < lowerWeight:
        lowerWeight = c[1]
        thinner.clear()
        thinner.append(c[0])
    elif c[1] == lowerWeight:
        thinner.append(c[0])

print(len(list))
print(fatter)
print(thinner)
