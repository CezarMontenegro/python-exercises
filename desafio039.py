#Faça um programa que leia o ano de nascimento de um jovem e 
# informe, de acordo com sua idade: 
# -Se ele ainda vai se alistar ao serviço militar. 
# -Se é a hora de se alistar. 
# -Se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou 
# que passou do prazo.

nascimento = int(input('Digite o ano de nascimento: '))
idade = 2021 - nascimento

if idade < 18:
    print('Ele ainda vai se alistar no serviço militar')
elif idade == 18:
    print('É a hora de se alistar no serviço militar')
elif idade > 18:
    print('Já passou do tempo do alistamento.')