import requests

def main():
	print('Consulta CEP!')
	print('-------------')
	print()

	cep_input = input('Digite o CEP para a consulta: ')

	if len(cep_input) != 8:
		print('Quantidade de digitos inválida, insira uma quantidade válida.')
		return cep_input

	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

	address_data = request.json()

	if 'erro' not in address_data:
		print('Informações do cep', cep_input)
		
		print('CEP: {}'.format(address_data['cep']))
		print('Logradouro: {}'.format(address_data['logradouro']))
		print('Complemento: {}'.format(address_data['complemento']))
		print('Bairro: {}'.format(address_data['bairro']))
		print('Cidade: {}'.format(address_data['localidade']))
		print('Estado: {}'.format(address_data['uf']))
		
	else:
		print('{}: O CEP informado é inválido!'.format(cep_input))

	print('---------------------------------')
	option = int(input('Deseja Consultar Outro CEP?\n1. Sim\n2. Sair\n==> '))
	if option == 1:
		main()
	else:
		print('Saindo...')


if __name__ == '__main__':
	main()