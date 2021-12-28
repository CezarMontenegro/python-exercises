#Desenvolva um programa que leia o primeiro termo e a razao de
# uma PA. No final, mostre os 10 primeiro termos de progressao

pt = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print(pt)

for c in range(1, 10):
    pt += razao
    print(pt)