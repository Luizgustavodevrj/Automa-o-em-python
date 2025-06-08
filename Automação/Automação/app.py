#================================================

#              Automação Bárbara

#================================================

'''
1 - Computador executa um arquivo .py em um horario programado
2 - Abre o chrome ---> Diario Oficial (FEITO)
3 - Clica no PDF
4 - Abre o PDF em outra janela
5 - Verifica se tem o nome
6 - Se achar:
        Notifica via Email
    Se não achar:
        Notifica via Email
'''

from webbrowser import open
from pyautogui import moveTo, click
from time import sleep
from downloads import baixado
from leitor import verificaNome
from enviar import envia

# Acesso ao Diário Oficial
url = "https://doweb.rio.rj.gov.br"
open(url)

# Esperar um momento
sleep(5.5)

# Baixa no PDF
moveTo(397, 496, duration=0.8)
click(button='left')

# Espera ser baixado
sleep(30)

# Identificar arquivo
arquivo = baixado()
nome = 'Nome'

# Acessar PDF
x = verificaNome(arquivo, nome)

# Enviar email
envia('email.com', x)



