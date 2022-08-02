"""
Python possui um módulo integrado chamado datetime - para trabalhar com data e hora
"""

import datetime

# print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MAXYEAR)

print(datetime.datetime.now)  # Informando data e hora atual

# replace() PARA FAZER AJUSTES NA DATA/HORA

inicio = datetime.datetime.now()

print(inicio)

#alterando o horario  par 16H EM PONTO

inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# CRIANDO DATA HORA

evento = datetime.datetime(2019,1, 1, 0)

print(evento)

# Recebendo dados do usuário e convertendo para data

nascimento = input('Informe sua data de nascimento (dd/mm/yyy):')

nascimento = nascimento.split('/') # Split separa, No caso pela /

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

# acessando individualmente os elementos de data e hora

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

 Manipulando Deltas de data e hora

'Delta = data_final - data_inicial'

import datetime

# Temos a data de hoje
data_hoje = datetime.datetime.now()
# Data para ocorrer um determinado evento

aniversario = datetime.datetime(2022, 10, 10, 0)

tempo_para_evento= aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(f'faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds //60 //60} horas...')

# Ecommerce Exemplo:

data_da_compra=datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
