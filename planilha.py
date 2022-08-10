import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyodbc import Error
import time
from datetime import date, datetime
import config

# Declarar variaveis
usuario = ''
senha = ''
url = ''

try:
    # Ler arquivo config.xlsx
    config = (config.planilha(usuario,senha,url))
    usuario = config[0]
    senha = config[1]
    url = config[2]

    # Instanciar Objeto Site
    navegador = webdriver.Chrome() 

    # Acessar site
    navegador.get(url)

    #Login Conta
    time.sleep(2)
    navegador.find_element('xpath','//*[@id="i0116"]').send_keys(usuario)
    navegador.find_element('xpath','//*[@id="idSIButton9"]').send_keys(Keys.ENTER)
    time.sleep(1)
    navegador.find_element('xpath','//*[@id="i0118"]').send_keys(senha)

    # Abrir Planilha
    time.sleep(2)
    navegador.find_element('xpath','/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input').send_keys(Keys.ENTER)
    navegador.find_element('xpath','/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input').send_keys(Keys.ENTER)
    navegador.maximize_window()
    print('Sucesso abrir arquivo...')

except Error as ex:
    print(f"Falha no Apontamento : ",ex)

# Fim Execução
finished = datetime.now()
print("Fim Execução: ",finished)