#Melhore o Desafio 061, perguntando para o usuário se ele quer 
#mostrar mais alguns termos. o programa encerra quando ele 
#disser que quer mostrar 0 termos

firstTerm = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
c = 1
moreTerms = 10

print(firstTerm)

while moreTerms != 0:
    while c < moreTerms:
        firstTerm += razao
        print(firstTerm)
        c += 1
    c = 0
    moreTerms = int(input('Quantos termos mais você quer mostrar? '))
