#Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se 
# o usuário quer ou não continuar. No final, mostre: 
# A) Quantas pessoas tem mais de 18 anos. 
# B) Quantos homens foram cadastrados. 
# C) Quantas mulheres tem menos de 20 anos

contadorIdade = 0
contadorHomem = 0
contadorMulher = 0
teste = ''

while teste != 'N':
    i = int(input('Digite sua idade aqui: '))
    s = input('Digite o sexo: ').upper()

    if i >= 18:
        contadorIdade += 1
    if s == 'M':
        contadorHomem += 1
    if s == 'F' and i <= 20:
        contadorMulher += 1

    teste = input('Deseja continar? [S/N] ').upper()
    

print(f'{contadorIdade} pessoas tem mais de 18 anos')
print(f'{contadorHomem} homens foram cadastrados')
print(f'{contadorMulher} mulheres com menos de 20 anos foram cadastradas')
