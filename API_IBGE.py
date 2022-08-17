
import json, requests

name_input= input("Insira o nome para pesquisa: ")

response = requests.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name_input}")

json_data = json.loads(response.text)

print(json_data)


