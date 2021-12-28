#Escreva um programa para aprovar o empréstimo bancário para a 
# compra de uma casa. O programa vai perguntar o valor da casa
#o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensa, sabendo que ela não pode
#exceder 30% do salário ou entáo o empréstimo será negado.

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
prazo = int(input('Digite o prazo do pagamento em anos: '))

mensalidade = salario * 0.3
prestacao = (casa / prazo) / 12

if prestacao > mensalidade:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')

