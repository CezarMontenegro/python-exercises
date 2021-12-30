#Crie um programa onde o usuário possa digitar vário valores 
# numéricos e cadastre-os em uma lista. Caso o número já exista 
# lá dentro, ele não será adicionado. No final, serão exibidos 
# todos os valores únicos digitados, em ordem cresecente.

valores = []

while True:
    n = (int(input('Digite um valor: ')))
    if n not in valores:
        valores.append(n)

    test = input('Deseja continuar? [S/N]').upper()
    if test == 'N':
        break

print(valores)