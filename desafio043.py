#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu IMC e mostre seu status, de acordo com a tabela baixo: 
# -Abaixo de 18.5: Abaixo do peso 
# -Entre18.5 e 25: Peso ideal 
# -25 até 30: Sobrepeso 
# -30 até 40: Obesidade 
# -Acima de 40: Obesidade mórbida

altura = float(input('Digite sua altura em M aqui: '))
peso = float(input('Digite seu peso em Kg aqui: '))

imc = peso / (altura ** 2)
print(imc)

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')