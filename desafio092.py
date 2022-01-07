 #Crie um programa que leia nome, ano de nascimento e carteira de 
 # trabalho e cadastre-os (com idade) em um dicionário se por acaso 
 # a ctps for diferente de zero, o dicionário receberá também o ano 
 # de contratação e o salário. Calcule e acrescente, além da idade, 
 # com quantos anos a pessoa vai se aposentar.

dicionario = {}

dicionario['nome'] = str(input('Digite o nome: '))
nascimento = int(input('Digite o ano de nascimento: '))
dicionario['idade'] = 2022 - nascimento 
ctps = int(input('Digite o número da ctps: '))

if ctps != 0:
    dicionario['contrato'] = int(input('Digite o ano de contratação: '))
    dicionario['salário'] = float(input('Digite o salário: '))

dicionario['aposentadoria'] = (70 - dicionario['idade']) + dicionario['contrato']

print(dicionario)
