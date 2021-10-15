import PySimpleGUI as sg
import json
import requests
#Acima estão as bibliotecas usadas no projeto.

#Class que configura os elementos que vão ser exibidos na tela.
class Ceptela:
    def __init__(self):
        #elementos do layout do programa.
        layout = [
                [sg.Text('Digite o cep que deseja buscar abaixo.')],
                [sg.Text('CEP'),sg.Input(size = (25,0), key='CEP')],
                [sg.Button('Buscar')],
                [sg.Output(size=(40,10))]
        ]

        self.tela = sg.Window('CEP Search',layout)
        self.button, self.values = self.tela.Read()

while True:
    window, event, values = sg.read_all_windows()
#Quando a janela for fechada....
    if window == Ceptela and event == sg.WIN_CLOSED:
        break
        
    #Define as váriaveis que consultam o cep e o exibem na sua tela.
    def consultarocep(self,cep):
    
        url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if url.status_code == 200:
        	print('Sucess')
        elif url.status_code == 400:
        	print('Erro')

        endereco = url.json()

        return endereco

    #Aqui ele formata os valores antes de exibir na tela do usuário.
    def mainwindow(self):
        while True:    
                
                
            self.button , self.values = self.tela.Read()
          
            try:    
                valores = self.consultarocep(self.values['CEP'])
                for k, v in valores.items():
                    print(k.upper() , ':' ,v)
               
            except:
                print('Name Error, Função não atribuida')
                

#Chama a função para a tela.
jn = Ceptela()
jn.mainwindow()