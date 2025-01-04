import pandas as pd

''' Qual foi o periodo e em qual(quais) estado(s) a gasolina ultrapassou a barreira dos R$ 5,00 '''

arquivo = pd.read_csv('gasolina_brasil.csv')

df = pd.DataFrame(arquivo)
df_2 = df[['ANO E MES', 'PREÇO MÉDIO REVENDA', 'ESTADO', 'PRODUTO']]
filtro = df_2[(df_2['PRODUTO'].isin(['GASOLINA COMUM', 'GASOLINA ADITIVADA'])) & (df_2['PREÇO MÉDIO REVENDA'] > 5 )]

df_3 = pd.DataFrame(filtro)
print(df_3)

periodo_ocorreu_aumento = df_3['ANO E MES'].value_counts()
estados_com_gasolina_superior_5 = df_3['ESTADO'].value_counts()

print(f'Periodo que ocorreu aumento:{periodo_ocorreu_aumento}')
print(f'Estados que mais tiveram aumento:{estados_com_gasolina_superior_5}')