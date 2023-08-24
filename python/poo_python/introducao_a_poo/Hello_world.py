hello = "Hello World!"
print(hello)
print(len(hello))
# print(hello.len())

import pandas as pd

# Criar um DataFrame com dados fictícios
data = {'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eve'],
        'Idade': [25, 30, 35, 40, 45],
        'Cidade': ['Nova York', 'Los Angeles', 'Chicago', 'Houston', 'Miami']}

df = pd.DataFrame(data)

# Exibir os primeiros registros do DataFrame
print("Primeiros registros:")
print(df.head())

# Obter informações sobre o DataFrame
print("\nInformações do DataFrame:")
print(df.info())

# Resumo estatístico das colunas numéricas
print("\nResumo estatístico:")
print(df.describe())

# Filtrar os registros com idade superior a 35
print("\nRegistros com idade superior a 35:")
print(df[df['Idade'] > 35])

# Ordenar o DataFrame por idade em ordem decrescente
print("\nDataFrame ordenado por idade:")
print(df.sort_values(by='Idade', ascending=False))