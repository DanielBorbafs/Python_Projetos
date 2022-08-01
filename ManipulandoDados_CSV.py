"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha
"""

from csv import writer
# O 'a' adiciona parametros ao csv
# O 'w' usado duas vezes apaga os dados anteriores
with open('filmes.csv', 'w', encoding='utf8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
            filme = input('informe o nome do filme:')
            if filme != 'sair':
                genero = input('informe o gênero:')
                duracao = input('Informe a duração (em minutos):')
                escritor_csv.writerow([filme, genero, duracao])


# DictWriter

from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Titulo', 'Genero', 'Duracao']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('informe o Genero: ')
            duracao = input('informe a duracao: ')
            escritor_csv.writerow({"Titulo": filme, "Genero": genero, "Duracao": duracao})
