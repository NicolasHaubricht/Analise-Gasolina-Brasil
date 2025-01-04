import pandas as pd

''' Qual o preço médio de revenda da gasolina em maio de 2014 em São Paulo? '''

arquivo = pd.read_csv('gasolina_brasil.csv')

df = pd.DataFrame(arquivo)
df_2 = df[['ANO E MES', 'PREÇO MÉDIO REVENDA', 'ESTADO', 'PRODUTO']]
filtro = df_2[(df_2['ANO E MES'] == '2014-05') & (df_2['ESTADO'] == 'SAO PAULO') & (df_2['PRODUTO'].isin(['GASOLINA COMUM', 'GASOLINA ADITIVADA']))]
df_3 = pd.DataFrame(filtro)
print(df_3)