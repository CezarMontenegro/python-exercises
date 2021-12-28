# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.

menores = 0
maiores = 0

for c in range(1, 8):
    n = int(input('Digite seu ano de nascimento: '))
    idade = 2021 - n
    if idade < 18:
        menores += 1
    else:
        maiores += 1

print('Das 7 pessoas {} são maiores.'.format(maiores))
print('Das 7 pessoas {} são menores.'.format(menores))
