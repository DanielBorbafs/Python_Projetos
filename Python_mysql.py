
# Criei um banco de dados simples com apenas duas colunas - Gênero e Nome do filme - O id é gerado automaticamente.


import mysql.connector # Após fazer a instalação utilizando o pipinstall - importamos o mysql
from mysql.connector import errorcode
import datetime


mydb = mysql.connector.connect(
    host="localhost",
    user="root",						# Script de conexão ao banco de dados
    password="",
    database="filmes"
)


try:
	db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='filmes')
	print("Conectado ao Banco de dados com Sucesso!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("O Banco de dados informado Não existe!")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Nome ou senha incorretos!")
	else:
		print(error)
else:
	db_connection.close()


mycursor = mydb.cursor() # definindo cursor para manusear a base de dados

mycursor.execute("Show tables;")  # mostrando todas tabelas do banco

myresult = mycursor.fetchall()

for x in myresult:  
	print(x)

# Inserindo dados na tabela
mycursor.execute("INSERT INTO catalogo (genero, nomefilme) VALUES ('suspense', 'A Cabana')")

# commitando para salvar todas alterações feitas
mydb.commit()

# Fechado o banco de dados
mydb.close()
