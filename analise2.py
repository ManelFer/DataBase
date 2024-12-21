# sigla_uf,id_municipio,nome_regiao,nome_empresa,porte_empresa,tecnologia,transmissao,acessos

import plotly.express as px
import pandas as pd

# importei os dados
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
tecnologias = nome_uf

# Filtragem do sistema
filtro_dados = dados[(dados['nome_uf'] == nome_uf) & (dados['nome_municipio'] == nome_municipio) & (dados['ano'].between(ano_inicial, ano_final)) & (dados['tecnologia'] == tecnologias)]


# trabalhar com os gráficos
tabela = px.data.medals_long()
tabela