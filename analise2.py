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

    # Gráfico de barra
    acessos_por_tecnologia = estado_data['tecnologia'].value_counts()
    plt.figure(figsize=(10, 6))
    acessos_por_tecnologia.plot(kind='bar')
    plt.title('distribuição de por tecnologia')
    plt.xlabel('Tecnologia')
    plt.ylabel('Número de acesso')
    plt.xticks(rotation=45)
    plt.savefig('acesso_por_tecnologia.png')
    plt.close()

    # Contanto acesso por ano
    acessos_por_ano = estado_data.groupby('ano')['nome_empresa'].count()
    plt.figure(figsize=(10, 6))
    acessos_por_ano.plot(kind='line')
    plt.title('Número de acesso por ano')
    plt.xlabel('ano')
    plt.ylabel('Número de acesso')
    plt.savefig('acesso_por_ano.png')
    plt.close()

    # maiores números
    acessos_por_empresa_porte = estado_data.groupby(['nome_empresa', 'porte_empresa']).size().reset_index(name='total_acessos')
    maiores_contratos = acessos_por_empresa_porte.sort_values(by='total_acessos', ascending=False)
    as_10_maiores_empresas = maiores_contratos.head(10)  # Exibe as 10 empresas com maior número de contratos
        # criando a tabela
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis('tight')
    ax.axis('off')
    tabela_data = as_10_maiores_empresas.values.tolist()
    columns = as_10_maiores_empresas.columns.tolist()
    table = ax.table(cellText=tabela_data, colLabels=columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False) 
    table.set_fontsize(10)
    table.scale(1.2, 1.2) # tamanho da tabela
    plt.title('As 10 maiores empresas', fontsize=14)
    plt.savefig('As_10_maiores.png', bbox_inches='tight')
    plt.close()

    # Contando acessos por ano e porte
    acessos_por_ano_porte = estado_data.groupby(['ano', 'porte_empresa']).size().unstack()
    acessos_por_ano_porte.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Mudança no Perfil das Empresas ao Longo dos Anos')
    plt.xlabel('Ano')
    plt.ylabel('Número de Acessos')
    plt.legend(title='Porte da Empresa')
    plt.savefig('perfil_empresas_ano.png')
    plt.close()

    # dados  recentes
    ano_recente = estado_data['ano'].max()
    dados_recente = estado_data[estado_data['ano'] == ano_recente]
    # Contagem de acessos
    acessos_recentes = dados_recente['nome_empresa'].value_counts().reset_index()
    acessos_recentes.columns = ['nome_empresa', 'total_acessos']  # Colunas 
    # iniciar tabela
    fig, ax = plt.subplots(figsize=(10, 4))  # Tamanho
    ax.axis('tight')
    ax.axis('off')
    table_data = acessos_recentes.values.tolist()  # Convertendo os dados para lista
    columns = acessos_recentes.columns.tolist()  # Obtendo os nomes das colunas
    table = ax.table(cellText=table_data, colLabels=columns, cellLoc='center', loc='center')
    # Estilizando a tabela
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)  # Ajustando o tamanho da tabela
    plt.title(f'Distribuição das Empresas em {ano_recente}', fontsize=14)
    plt.savefig('distribuicao_empresas_tabela.png', bbox_inches='tight')  
    plt.close()  


# Analisar o estado escolhido
analisar_estado(estado_escolhido, ano_inicial, ano_final)