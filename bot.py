from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyodbc import Error
import time
from datetime import date, datetime
import pandas as pd
import config
from tkinter import *
from tkinter import messagebox


# Inicio Execução
started = datetime.now()
print("Inicio Execução: ",started)

# Declarar variaveis
usuario = ''
senha = ''
url = ''
carga_hora = ''

###Gera a Tela para entrada de dados na tela

# Função onde recebe a carga apos confirmada.
def carga_horaria():
    if carga.get() == '':
        messagebox.showinfo(title="Erro",message="Informe a carga horária nesse padrão -  HH:MM")
    global armazenar_carga
    armazenar_carga = carga.get()
    # Fecha a tela.
    if armazenar_carga != '':
        print("Carga horária informada: %s"%carga.get())
        carga.delete(0, "end")
        app.destroy()

# Formatando a Tela    
app = Tk()
app.title("CARGA HORÁRIA -  HH:MM")
app.geometry("320x120+620+200")
app.resizable(0,0)
app.configure(background="#dde")

Label(app,text="Carga horária",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=80,height=20)

# Variavel recebe o valor informado
carga = Entry(app)
carga.focus()
carga.insert(0, "08:00")
carga.place(x=100, y=10,width=50,height=20)

# Define o botão Confirmar
btn_confirmar = Button(app,text="Confirmar",command=carga_horaria).place(x=110,y=70,width=100,height=20)

# Garante que a tela fique aparecendo, fica executando...
app.mainloop()

# Atribui o valor digitado no input da Tela
carga_hora = armazenar_carga

# time.sleep(3600) #### aguardar 1 hora ####

try:
    # Ler arquivo config.xlsx
    config = (config.trading(usuario,senha,url))
    usuario = config[0]
    senha = config[1]
    url = config[2]

    # Instanciar Objeto Site
    navegador = webdriver.Chrome()

    # Acessar site
    navegador.get(url)

    # Fazer Login
    navegador.find_element('xpath','//*[@id="Body_Body_txtUserName"]').send_keys(usuario)
    navegador.find_element('xpath','//*[@id="Body_Body_txtPassword"]').send_keys(senha)
    navegador.find_element('xpath','//*[@id="Body_Body_LoginButton"]').send_keys(Keys.ENTER)
    print('Login realizado')

    # Navegar para pagina TimeSheet
    navegador.get('https://app.tradingworks.net/Activities/ManualTimeSheet.aspx')

    # Selecionar Projeto
    navegador.find_element('xpath','//*[@id="cmbProjects"]').send_keys(Keys.ENTER)
    navegador.find_element('xpath','//*[@id="cmbProjects"]').send_keys('Usi')
    navegador.find_element('xpath','//*[@id="cmbProjects"]').send_keys(Keys.ENTER)

    # Selecionar Tipo Serviço
    navegador.find_element('xpath','//*[@id="cmbActivities"]').send_keys(Keys.ENTER)
    navegador.find_element('xpath','//*[@id="cmbActivities"]').send_keys('Des')
    navegador.find_element('xpath','//*[@id="cmbActivities"]').send_keys(Keys.ENTER)
    print('Projeto e tarefa informada.')

    # Informar Carga Horaria
    time.sleep(2)
    navegador.find_element('xpath','//*[@id="Body_Body_txtHours"]').send_keys(armazenar_carga)
    navegador.find_element('xpath','//*[@id="Body_Body_btnAddActivity"]').send_keys(Keys.ENTER)
    print('Carga horaria apontada.')

    # Fazer Logoff
    navegador.find_element('xpath','//*[@id="form1"]/div[3]/div/div[2]/ul[2]/li[3]/a').send_keys(Keys.ENTER)
    navegador.find_element('xpath','//*[@id="Body_btnLogOut"]').send_keys(Keys.ENTER)

    # Fechar Site
    navegador.close()
    print('Apontamento realizado com sucesso !!!')

except Error as ex:
    print(f"Falha no Apontamento : ",ex)

# Chama a Planilha
# Colocar a planilha dentro do diretorio na sua maquina e mudar no config.xlsx
import planilha

