#Elabora um programa que calcule o calor a ser pago por um produto,
# considerando o seu preco normal e condicao de pagamento: 
# -A vista dinheiro/cheque: 10% 
# -A vista no cartáo: 5% 
# -Em até 2x no cartao: preco normal 
# -3x ou mais no cartao 20% de juros

preco = float(input('Digite o preço do produto: '))

print('1 - A vista')
print('2 - A vista no cartão')
print('3 - Em 2x no cartão')
print('4 - Em 3x ou mais no cartão')

condicao = int(input('Digite a condição de pagamento desejada: '))

if condicao > 4:
    print('1 - A vista')
    print('2 - A vista no cartão')
    print('3 - Em 2x no cartão')
    print('4 - Em 3x ou mais no cartão')
    condicao = int(input('Escolha uma das condiçoes acima: '))

if condicao == 1:
    print('O preço com 10%, de desconto é {}'.format(preco * 0.9))
elif condicao == 2:
    print('O preço com 5%, de desconto é {}'.format(preco * 0.95))
elif condicao == 3:
    print('O preço sem desconto é {}'.format(preco))
elif condicao == 4:
    print('O preco com juros é {}'.format(preco * 1.2))