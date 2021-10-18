import requests
#importei a biblioteca sys para não dar erro na hora de passar pra .exe
import sys

#Função Principal que chama o programa e da ao usuário as informações.
def main():
	print('Consulta CEP!')
	print('-------------')
	print()
    #Onde o usuário coloca o cep que deseja.
	cep_input = input('Digite o CEP para a consulta: ')
    #Para o programa não crashar caso tenha mais de 8 digitos no CEP.
	if len(cep_input) != 8:
		print('Quantidade de digitos inválida, insira uma quantidade válida.')
		return cep_input
    #Aqui a biblioteca faz a requisição do cep para o site.
	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    #Aqui também.
	address_data = request.json()
    #Aqui ele diz que caso não tenha erro, jogue tais informações na tela do usuário.
	if 'erro' not in address_data:
		print('Informações do cep', cep_input)
		
		print('CEP: {}'.format(address_data['cep']))
		print('Logradouro: {}'.format(address_data['logradouro']))
		print('Complemento: {}'.format(address_data['complemento']))
		print('Bairro: {}'.format(address_data['bairro']))
		print('Cidade: {}'.format(address_data['localidade']))
		print('Estado: {}'.format(address_data['uf']))
	#Mais uma proteção caso o CEP seja inválido.	
	else:
		print('{}: O CEP informado é inválido!'.format(cep_input))
    #Estrutura de decisão para que o usuário possa escolher se deseja consultar outro cep!
	print('---------------------------------')
	option = int(input('Deseja Consultar Outro CEP?\n1. Sim\n2. Sair\n==> '))
	if option == 1:
		main()
	else:
		print('Saindo...')
        sys.exit()


if __name__ == '__main__':
	main()