import pandas as pd

''' Crie uma nova coluna para representar o ano e o mês(aaaa-mm), utilizando a coluna DATA FINAL como referência '''

arquivo = pd.read_csv('gasolina_brasil.csv')

df_final = pd.Series(data=arquivo['DATA FINAL'])
nova_coluna = pd.to_datetime(df_final)
nova_coluna = nova_coluna.dt.strftime('%Y-%m')
arquivo['ANO E MES'] = nova_coluna
arquivo.to_csv('gasolina_brasil.csv')
print(arquivo['ANO E MES'])