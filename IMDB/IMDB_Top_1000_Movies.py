import pandas as pd
import numpy as np

# Carregar o dataset em repositório do Github
url = 'https://raw.githubusercontent.com/merveser/IMDB_Data_Analysis/main/imdb_top_1000.csv'
df = pd.read_csv(url)

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Colunas de avaliação
colunas_numericas = ['IMDB_Rating', 'Meta_score', 'Gross']

# Remover valores ausentes e converter para tipo numérico
df['Gross'] = df['Gross'].str.replace(',', '').astype(float)  # Remover vírgulas e converter para float
df = df.dropna(subset=colunas_numericas)

# Principais funções sobre avaliações
for coluna in colunas_numericas:
    dados = df[coluna].to_numpy()
    media = np.mean(dados)
    mediana = np.median(dados)
    desvio_padrao = np.std(dados, ddof=1)
    minimo = np.min(dados)
    maximo = np.max(dados)
    
    print(f'\nEstatísticas para {coluna}:')
    print(f'Média: {media}')
    print(f'Mediana: {mediana}')
    print(f'Desvio Padrão: {desvio_padrao}')
    print(f'Mínimo: {minimo}')
    print(f'Máximo: {maximo}')
