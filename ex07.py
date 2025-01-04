import pandas as pd

''' Filtre o DataFrame para obter apenas dados da 'GASOLINA COMUM' '''

arquivo = pd.read_csv('gasolina_brasil.csv')

df = pd.DataFrame(arquivo)
filtro_gasolina_comum = df['PRODUTO'] == 'GASOLINA COMUM'
print(df[filtro_gasolina_comum])