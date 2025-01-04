import pandas as pd

'''  Carregue os conjuntos de dados "gasolina_2000+.csv" e "gasolina_2010+.csv" em dois DataFrames diferentes e combine-os em um único DataFrame. '''

df1 = pd.read_csv('gasolina_2000+.csv')
df2 = pd.read_csv('gasolina_2010+.csv')
df3 = pd.concat([df1, df2])
print(df3)