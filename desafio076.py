#Crie um programa que tenha um tupla única com nomes de produtos e 
#respectivos preços, na sequência. No final, mostre uma listagem 
#de preços, organizndo os dados em forma tabular.

lista = (
    'Lápis', 1.75,
    'Borracha', 2, 
    'Caderno', 15.90, 
    'Estojo', 25
)

for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end = '')
    else:
        print(f'R${lista[c]: >10}')


 