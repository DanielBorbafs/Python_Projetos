

from datetime import date
from datetime import datetime


# Convertendo data para string
def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str) -> date:  # Formatando para data e hora.
    return datetime.strptime(data, '%d/%m/%Y')

# Formatando valores para moeda 'REAL'
def formata_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'

