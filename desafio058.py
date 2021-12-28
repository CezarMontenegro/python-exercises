#Melhore o jogo do desafio028 onde o computador vai 'Pensar'em um
#número entre 0 e 10. só que agora o jogador vai tentar adivinhar até
#até acertar, mostrando no final quantos palpites foram necessario
#para vencer.

from random import randint

aleatory = randint(1, 10)
user = int(input('Digite seu palpite: '))
contador = 1

while aleatory != user:
    contador += 1
    user = int(input('Você errou, tente outra vez! '))
print('Parabéns você acertou, você precisou de {} tentativas'.format(contador))
