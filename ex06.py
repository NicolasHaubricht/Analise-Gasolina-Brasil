import pandas as pd

''' Utilizando o value_counts(), liste todos os tipos de produtos contidos na base de dados '''

arquivo = pd.read_csv('gasolina_brasil.csv')

df = pd.DataFrame(data=arquivo['PRODUTO'].value_counts())
print(df)