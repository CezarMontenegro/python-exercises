#Crie um programa onde o usuário digite uma expressão qualquer 
# que use parenteses. Seu aplicativo deverá analisar se a 
# expressão passada está com os parenteses abertos e fechados na 
# ordem correta

string = str(input('Digite sua expressão: '))
parenteses = []

for c in string:
	if c == '(':
		parenteses.append(c)
	elif c == ')':
		if len(parenteses) != 0:
			parenteses.pop()
		else:
			parenteses.append(c)
			break
if len(parenteses) == 0:
	print('A expressão está correta')
else:
	print('A expressao está incorreta')
			