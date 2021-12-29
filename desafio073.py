#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela 
# Campeonato Brasileiro de Futebol de 2021, na ordem de colocação. Depois mostre:
# A)Apenas os 5 primeiros colocados. 
# B)Os últimos 4 colocados da tabela. 
# C)Uma lista com os times em ordem alfabética 
# D)Em que posicão na tabela está o time da Chapecoense

times = ('Atlético Mineiro',
    'Flamengo',
    'Palmeiras',
    'Fortaleza',
    'Corinthians',
    'Bragantino',
    'Fluminense',
    'América-MG',
    'Atlético Goianiense',
    'Santos',
    'Ceará',
    'Internacional',
    'São Paulo',
    'Athletico-PR',
    'Cuiabá',
    'Juventude',
    'Grêmio',
    'Bahia',
    'Sport Recife',
    'Chapecoense',
)

posicaoChape = times.index('Chapecoense') + 1

print(times[0:5])
print(times[-4:])
print(sorted(times))
print(f'A Chapecoense está na posicão {posicaoChape}.')
