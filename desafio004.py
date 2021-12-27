#Faça um programa que leia algo pelo teclado e mostre na tela
#seu tipo primitivo  e todas as informações possiveis sobre ele.

var = input('Digite aqui:')

print('O tipo primitivo desse valor é: ', type(var))
print('Esse valor é numérico? ', var.isnumeric())
print('Esse valor é alfanumérico? ', var.isalnum())
print('Esse valor e alfabetico? ', var.isalpha())
print('Esse valor é decimal? ', var.isdecimal())
print('Esse valor está em maisculas? ', var.isupper())
print('Esse valor está em minusculas? ', var.islower())
print('Esse valor está capitalizado? ', var.istitle())
print('Esse valor é um digito?', var.isdigit())
print('Esse valor é um identificador?', var.isidentifier())
print('Esse valor é imprimivel?', var.isprintable())
print('Esse valor é somente espaços?', var.isspace())
