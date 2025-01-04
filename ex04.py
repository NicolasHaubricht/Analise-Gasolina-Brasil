import pandas as pd

'''  Você deve ter percebido que as colunas DATA INICIAL e DATA FINAL estão formatadas como string. Utilizando o método pd.to_datetime(), converta ambas colunas para Timestamp / Datetime '''

arquivo = pd.read_csv('gasolina_brasil.csv')    

df_inicial = pd.Series(data=arquivo['DATA INICIAL'])
df_final = pd.Series(data=arquivo['DATA FINAL'])
print(pd.to_datetime(df_inicial))
print(pd.to_datetime(df_final))