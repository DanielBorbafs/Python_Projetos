# Fiz esse código afins de estudo, ele informa dados 'fakes' automáticos. e logo após transforma o arquivo em JSON
'OBS: Falta refatorar!'

# biblioteca para trabalhar com json
import jsonpickle
# Biblioteca para trabalhar com dados fakes
from faker import Faker
# Puxando a função
fake = Faker()

class Dadosfk:
    def __init__(self, nomemasculino, nomefeminino, usuario, senha, data):
        self.__nomemasculino = nomemasculino
        self.__nomefeminino = nomefeminino
        self.__usuario = usuario
        self.__senha = senha
        self.__data = data

    @property
    def nomemasculino(self):
        return self.__nomemasculino

    @property 
    def nomefeminino(self):
        return self.__nomefeminino.fake.first_name_female()  # criando class e acessando cada propriedade (Logo menos irei refatorar)

    @property
    def usuario(self):
        return self.__usuario
    
    @property
    def senha(self):
        return self.__senha

    @property
    def data(self):
        return self.__data

nomemasculino = fake.first_name_male()

nomefeminino = fake.first_name_female()

usuario = fake.user_name()              # push de dados fakes

senha = fake.password()

data = fake.date()

Fakedd = Dadosfk(nomemasculino, nomefeminino, usuario, senha, data)

ret = jsonpickle.encode(Fakedd)

with open('Fakedd.json', 'w') as arquivo:
    ret = jsonpickle.encode(Fakedd)
    arquivo.write(ret)

with open('Fakedd.json', 'r') as arquivo:
   conteudo = arquivo.read()
   ret = jsonpickle.decode(conteudo)
   print(ret)
