import requests


def main():
    print('Bem vindo')
    coin_input = input('Digite a moeda para a consulta:')


    request = requests.get(f'https://api.coincap.io/v2/assets/{coin_input}')


    address_data = request.json()

    if 'erro' not in address_data:
        print('==> Buscando moeda... <==')
        print('A moeda foi {}'.format(coin_input))
        print(f'{address_data}')
        
        
        def Coleta():
        infos = address_data
        ret = jsonpickle.encode(infos)
        print(ret)
        with open('criptos.json','w') as arquivo:
            ret = jsonpickle.encode(infos)
            arquivo.write(ret)
    Coleta()






if __name__ == '__main__':
    main()

    
    ### DIFICULDADE PARA PUXAR SÒ O NECESSÀRIO NO JSON >> PRECISO PENSAR UMA FORMA DE PUXAR SOMENTE O ID, PriceUSD, Name e ID.
