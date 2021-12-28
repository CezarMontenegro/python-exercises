#Refaça o desafio -51, lendo o primeiro termo e a razão de um PA, 
# mostrando os 10 primeiros termos da progressão usando a 
# estrutura while.

firstTerm = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
c = 1

print(firstTerm)
while c < 10:
    firstTerm += razao
    print(firstTerm)
    c += 1