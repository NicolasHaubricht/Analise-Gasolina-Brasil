import pandas as pd

'''  Qual o preço médio de revenda da gasolina em agosto de 2008? '''

arquivo = pd.read_csv('gasolina_brasil.csv')

df = pd.DataFrame(arquivo)
df_2 = df[['ANO E MES', 'PREÇO MÉDIO REVENDA']]
filtro = df_2[df_2['ANO E MES'] == '2008-08']
print(filtro)
print('Preço Médio de Revenda em Agosto de 2008: R$', filtro['PREÇO MÉDIO REVENDA'].mean())