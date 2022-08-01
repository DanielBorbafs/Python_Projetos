
" CSV - Comma Separated Values - Valores separados por vírgulas "
# Estou usando txt por enquanto pois meu notebook está bugado com arquivos CSV, Ja estou resolvendo.

# Abrindo o arquivo - tem que estar no mesmo diretório
with open('ler.txt') as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    dados = dados.split(',') # Separando por vírgula
    print(dados)

# Reader
'Reader permite que iteremos sobre as linhas do CSV como Listas'
from csv import reader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        # cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros')


# DictReader
'DictReader permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts'
from csv import DictReader

with open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")


# Quando estiver com outro separador sem ser vírgulas, utlizar esse comando :
 leitor_csv = DictReader(arquivo, delimiter=', ou . ou = ') # Qualquer outro separador utilizar esse ocmen
