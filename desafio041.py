#A Confederação Nacional de Nataçao precisa de um programa que 
# leia o ano de nascimento de um atleta e mostre sua categoria, 
# de acordo coma idade: 
# -Até 9 anos: Mirim 
# -Até 14 anos: Infantil 
# -Até 19 anos: Junior 
# -Até 20 anos: Senior 
# -Acima: Master

nascimento = int(input('Digite o ano de nascimento do atleta aqui: '))
idade = 2021 - nascimento

if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif idade == 20:
    print('SENIOR')
elif idade > 20:
    print('MASTER')