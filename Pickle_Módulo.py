"""
Pickle - Realiza os processos:
Objeto Python -> Binarização
Binarização -> Objeto Python

este processo é chamado de serialização/descerialização

#OBS: O módulo Picle não é seguro contra dados maliciosos, dessa forma tomar cuidado ao manipular arquivos
pickle de fontes desconhecidas.
"""

import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def comer(self):
        print(f'{self.__nome} está comendo')


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} Este animal mia')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} Este animal late')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('teste.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)


# Fazer Leitura em arquivos pickle

with open('teste.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato._Animal__nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro._Animal__nome}')
    cachorro.late()
    print(f'O tipo de cachorro é {type(cachorro)}')
