import pandas as pd

''' Selecione a terceira entrada da coluna DATA INICIAL e verifique seu tipo '''

arquivo = pd.read_csv('gasolina_brasil.csv')    

df_inicial = pd.Series(data=arquivo['DATA INICIAL'], index=['2004-05-09'])
print(df_inicial)