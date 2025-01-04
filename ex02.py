import pandas as pd

''' Investigue as colunas e entenda o conjunto de dados usando o head() e info() '''

arquivo = pd.read_csv('gasolina_brasil.csv')

for colunas in arquivo.columns:
    df = pd.DataFrame(data=arquivo[colunas])
    print(df.info())
    print(df.head(3))