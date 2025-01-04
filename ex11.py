import pandas as pd

''' Qual foi a média de preço dos estados da região sul em 2012? '''

arquivo = pd.read_csv('gasolina_brasil.csv')

df = pd.DataFrame(arquivo)
df_2 = df[['ANO E MES', 'PREÇO MÉDIO REVENDA', 'REGIÃO', 'PRODUTO']]
filtro = df_2[(df_2['REGIÃO'] == 'SUL') & (df_2['ANO E MES'] >= '2012-01') & (df_2['ANO E MES'] <= '2012-12') & (df_2['PRODUTO'].isin(['GASOLINA COMUM', 'GASOLINA ADITIVADA']))]
filtro = pd.DataFrame(filtro)
print(filtro)
print('Preço Médio de Revenda da gasolina nos Estados do Sul no ano de 2012: R$', filtro['PREÇO MÉDIO REVENDA'].mean())