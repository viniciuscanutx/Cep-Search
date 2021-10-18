import requests 

print('ConsultaCEP')
print('-----------')

cep_input = input('Insira seu CEP aqui: ')

if len(cep_input) != 8:
    print('Quantidade de Digitos Inválida!')
    exit()
    
request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

andress_data = request.json()