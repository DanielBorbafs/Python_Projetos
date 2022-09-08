import mysql.connector
from mysql.connector import errorcode
import datetime


mydb = mysql.connector.connect(
    host="localhost",
    user="root",						# Script de conexão ao banco de dados
    password="",
    database="rh"
)


def cadastro(conexao):
    print("digite os dados do colaborador \n")
    nome = input("Nome ")
    nascimento =input("Telefone  ")
    cpf =input("Cpf: ")
    rg = input("RG :")
    nacionalidade = input("Nacionalidade: ")
    estado = input("Estado: ")
    bairro = input("Bairro: ")
    rua_avenida =input("Rua_avenida: ")
    numero = input("Numero")
    cep = input("CPF")
    sql="insert into colaboradoes (nome, nascimento, cpf, rg, nacionalidade, estado, bairro, rua_avenida, numero, cep) values ('"+nome+"', '"+nascimento+"', '"+cpf+"', '"+rg+"', '"+nacionalidade+"', '"+estado+"', '"+bairro+"', '"+rua_avenida+"', '"+numero+"', '"+cep+"')"
    mycursor = mydb.cursor()
    try:
        mycursor.execute(sql)
        conexao.commit()
        print('Dados gravados com sucesso')
    except cadastro() as error:
        print('ERROR')
    conexao.close()


