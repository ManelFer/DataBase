import matplotlib
matplotlib.use('Agg')  # Altere para um backend que não dependa do tkinter
import pandas as pd
import matplotlib.pyplot as plt

# URL do arquivo CSV
url = "https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv"

# Lendo os dados do CSV
data = pd.read_csv(url)

# Convertendo a coluna 'ano' para string para facilitar a filtragem
data['ano'] = data['ano'].astype(str)

# Exibir as colunas disponíveis
print("As unidades Federativas disponíveis são:")
print(data[['sigla_uf']].drop_duplicates())

# escolher o estado
estado_escolhido = input('Escolha uma Unidade Federativa (UF): ')

# Solicitar intervalo de datas
ano_inicial = input('Digite o ano inicial (ex: 2018): ')
ano_final = input('Digite o ano final (ex: 2020): ')

# Função para analisar os dados de um estado específico
def analisar_estado(estado, ano_inicial, ano_final):
    # Filtrando os dados para o estado escolhido e o intervalo de anos
    estado_data = data[(data['sigla_uf'] == estado) & 
                       (data['ano'] >= ano_inicial) & 
                       (data['ano'] <= ano_final)]
    
    if estado_data.empty:
        print(f"Nenhum dado encontrado para o estado: {estado} no intervalo de {ano_inicial} a {ano_final}.")
        return
    
    # Exibindo algumas informações básicas
    print(f"Análise de dados para o estado: {estado} de {ano_inicial} a {ano_final}")
    print(f"Número total de registros: {len(estado_data)}")
    
    # Contando o número de acessos por empresa
    acessos_por_empresa = estado_data['nome_empresa'].value_counts()
    print("\nNúmero de acessos por empresa:")
    print(acessos_por_empresa)
    
    # Gráfico de pizza
    plt.figure(figsize=(10, 6))
    plt.pie(acessos_por_empresa, labels=acessos_por_empresa.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'Acesso às empresas do estado de {estado} de {ano_inicial} a {ano_final}')
    plt.axis('equal')  # Para o gráfico ficar igual
    plt.savefig('grafico_pizza.png')  # Salva o gráfico como imagem
    plt.close()  # Fecha a figura

# Analisar o estado escolhido
analisar_estado(estado_escolhido, ano_inicial, ano_final)