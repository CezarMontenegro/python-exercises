#Faça uma tabuada com o número escolhido pelo usuário

n = int(input('Digite o inteiro: '))

for c in range(1, 10):
    print('{} x {} = {}'.format(n, c, c * n ))