### Este Script trata do arquivo config.xlsx. Aqui você pode setar todos os parametros necessários para a automação;
### Sempre informar o caminho do arquivo excel;
### Caso faça uma melhoria lembre-se de atualizar o original.

from pyodbc import Error
import pandas as pd

try:
     # Ler arquivo config.xlsx
    def trading(usuario,senha,url):
        arquivo = pd.read_excel(r'C:\Projetos\tradingworks\config.xlsx')
        usuario=(arquivo['usuario'][0])
        senha=(arquivo['senha'][1])
        url=(arquivo['url'][1]) 
        return usuario,senha,url

    def planilha(usuario,senha,url):
        arquivo = pd.read_excel(r'C:\Projetos\tradingworks\config.xlsx')
        usuario=(arquivo['usuario'][0])
        senha=(arquivo['senha'][0])
        url=(arquivo['url'][0]) 
        return usuario,senha,url

except Error as ex:
    print("Falha na leitura do arquivo config ",ex)