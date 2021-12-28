#Crie um programa que leia duas notas de um aluno e calcule
# sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# -Média abaixo de 5.0: Reprovado
# -Média aentre 5.0 e 6.9: Recuperação
# -Média 7.0 ou superior: Aprovado

n1 = float(input('Digite sua n1 aqui: '))
n2 = float(input('Digite sua n2 aqui: '))

media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO')
elif 5 <= media < 7:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO') 