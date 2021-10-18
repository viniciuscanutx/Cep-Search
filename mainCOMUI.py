from PySimpleGUI.PySimpleGUI import WIN_CLOSED
import requests
import json
import PySimpleGUI as sg
import sys


class ceptela:
 def __init__(self):
    
    layout = [
            [sg.Text('CEP'),sg.Input(size = (25,0), key='CEP')],
            [sg.Button('Buscar')],
            [sg.Output(size=(40,10))]
    ]


    self.tela = sg.Window('Busca de CEP',layout)
    self.button, self.values = self.tela.Read()
 
 
 def consultacep(self,cep):

        url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        if url.status_code == 200:
        	print('Informações Sobre o CEP abaixo.')
        elif url.status_code == 400:
        	print('Erro 400')

        endereco = url.json()

        return endereco


 def start_window(self):
        while True:
                
            self.button , self.values = self.tela.Read()
                
            try:    
                valores = self.consultacep(self.values['CEP'])
                for k, v in valores.items():
                    print(k.upper() , ':' ,v)

            except:
                print('Função Não Definida.')
                


                

jn = ceptela()
jn.start_window()
