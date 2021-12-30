 # Crie um programa que vai ler vários números e colocar em uma 
 # lista. Depois disso, mostre: 
 # A)Quantos números foram digitados. 
 # B)A lista de valores, ordenada de forma decrescente. 
 # C)Se o valor 5 foi digitado e está ou não na lista.

values = []
test = ''

while test != 'N':
    n = int(input('Digite um valor:'))
    test = input('Deseja continar? [S/N]').upper()

    if len(values) == 0 or n < values[-1]:
        values.append(n)
    else:
        pos = 0
        while True:
            if n >= values[pos]:
                values.insert(pos, n)
                break
            pos += 1
print(len(values))
print(values)
print(5 in values)

            
