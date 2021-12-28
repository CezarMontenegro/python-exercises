#Escreva um programa que pergunte o saário de um funcionário e 
#calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.

sal = float(input('Digite o salário: '))

if sal > 1250:
    sal = sal * 1.1
    print(sal)
else:
    sal = sal * 1.15
    print(sal)


