import requests

def main():
    print("##### BUSCANDO CEP #####")
    print()

    cep_input = input('Digite o CEP para a consulta: ') # Obtendo cep do usuário

    if len(cep_input) != 8:  # se o numero de digitos  for diferente de 8
        print('Quantidade de dígitos inválida!')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input)) #Format para usar dados do input

    address_data = request.json() # Aqui acontece um erro (caso o cep for 8 numeros porém invalido)

    if 'erro' not in address_data:
        print('==> CEP ENCONTRADO <==')

        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))   # EXIBINDO DE FORMA MAIS AGRÁDAVEL
        print('Estado: {}'.format(address_data['uf']))

    else:
        print('{}: CEP inválido.'.format(cep_input))

    print('---------------------------------')
    option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
    if option == 1:
        main()
    else:
        print('Saindo...')


if __name__ == '__main__':
    main()
