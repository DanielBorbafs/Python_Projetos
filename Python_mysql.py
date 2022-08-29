
import mysql.connector # Após fazer a instalação utilizando o pipinstall - importamos o mysql
from mysql.connector import errorcode
import datetime




mydb = mysql.connector.connect(
    host="localhost",
    user="root",						# Script de conexão ao banco de dados
    password="",
    database="filmes"
)




# Atribuindo variável ao cursor para manusear a database
mycursor = mydb.cursor()

mycursor.execute("Show tables;")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)

# Inserindo dados na tabela
insere_nome = input('Digite o nome do filme')
insere_genero = input('Digite o gênero')

mycursor.execute(f"INSERT INTO catalogo (nome, genero) VALUES ('{insere_nome}', '{insere_genero}')")

# commitando para salvar todas alterações feitas
mydb.commit()

# Fechado o banco de dados
mydb.close()
