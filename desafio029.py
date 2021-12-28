#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
#foi multado.
#A multa vai custar R$7,00 por cada km acima do limite.

vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    excedente = vel - 80
    multa = (excedente) * 7
    print('Você esta {}km acima do limite, sua multa é de: R${}'.format(excedente, multa))