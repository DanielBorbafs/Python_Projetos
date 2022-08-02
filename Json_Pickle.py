"""
JSON > JavaScript Object Notation

API > Meio de comunicação entre serviços oferecidos por empresas
"""


import jsonpickle

class Game:
    def __init__(self, nome, genero):
        self.__nome = nome
        self.__genero = genero

    @property
    def nome(self):
        return self.__nome

    @property
    def genero(self):
        return self.__genero


suspense = Game('Call of Duty', 'Ação')

ret = jsonpickle.encode(suspense)

print(ret)

# para integrar json com Pickle. - pip install jsonpickle

#REFATORANDO

with open('suspense.json', 'w') as arquivo:
    ret = jsonpickle.encode(suspense)
    arquivo.write(ret)

# Lendo o arquivo

with open('suspense.json', 'r') as arquivo:
   conteudo = arquivo.read()
   ret = jsonpickle.decode(conteudo)
   print(ret)
   print(type(ret))
   print(ret.nome)
   print(ret.genero)
