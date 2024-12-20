import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Corrigido para importar pyplot

# Carregar os dados
dados = pd.read_csv('https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv')

# Exibir as colunas disponíveis para o usuário
print("Colunas disponíveis:")
print(dados[['nome_uf', 'nome_municipio']].drop_duplicates())

# Input para o usuário escolher o que vai receber
nome_uf = input('Escolha uma Unidade Federativa (UF): ')
nome_municipio = input('Escolha um Município: ')
ano_inicial = 2021
ano_final = 2022
ano_total = ano_inicial + ano_final

# Filtragem do sistema
filtro_dados = dados[(dados['nome_uf'] == nome_uf) & (dados['nome_municipio'] == nome_municipio) & (dados['ano'].between(ano_inicial, ano_final))]

# Exibir o resultado
if not filtro_dados.empty:
    print("Seu resultado foi:")
    print(filtro_dados)
else:
    print("Nenhum dado encontrado para a combinação escolhida.")

# Exibir a primeira linha do DataFrame
# print(dados.head(10))

# Exibir informações dos DataFrames
# print(dados.info())

# Exibir estatísticas descritivas
# print(dados.describe())

# Filtro da cidade