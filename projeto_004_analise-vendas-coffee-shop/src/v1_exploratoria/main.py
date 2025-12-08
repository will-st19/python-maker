import pandas as pd
import matplotlib.pyplot as plt

FILEPATH = 'data/Coffee Shop Sales.xlsx'

try:
    # Usar pd.read_excel para arquivos Excel
    # Se o arquivo tiver várias planilhas, pode ser necessário especificar `sheet_name='Nome da Planilha'`
    df = pd.read_excel(FILEPATH)
    
    # 1. Mostrar as 5 primeiras linhas
    print("✅ Leitura do Excel bem-sucedida! Primeiras 5 linhas:")
    print(df.head())
    
    # print("\n---")
    
    # 2. Verificar a estrutura (tipos de dados e nulos)
    # print("🔍 Informações da Estrutura (Tipos de Dados e Nulos):")
    # df.info()

except FileNotFoundError:
    print(f"❌ Erro: O arquivo '{FILEPATH}' não foi encontrado.")
except ImportError:
    print("❌ Erro: A biblioteca 'openpyxl' não está instalada.")
    print("Por favor, execute: pip install openpyxl")
except Exception as e:
    print(f"❌ Ocorreu um erro durante a leitura do arquivo: {e}")

# ---------------------------------------------------------------------- #

def get_daily_sales_trend(df):
    """
    Calcula o faturamento total diário para visualizar a tendência ao longo do tempo.
    
    Argumento:
        df (DataFrame): O DataFrame de vendas com a coluna 'Revenue'.
        
    Retorna:
        DataFrame: Faturamento total agrupado por dia.
    """
    # Agrupa por 'transaction_date' (o dia da venda) e soma o 'Revenue'
    daily_revenue = df.groupby('transaction_date')['Revenue'].sum().reset_index()
    
    # Renomeia a coluna para clareza
    daily_revenue.columns = ['Date', 'Daily_Revenue']
    
    # Exibe o começo da tendência
    print("📈 Tendência Diária de Vendas (Primeiros 5 dias):")
    print(daily_revenue.head())
    
    # Este resultado deve ser usado para gerar o gráfico de linha (Matplotlib)
    return daily_revenue

# ---------------------------------------------------------------------- #

def plot_sales_trend(daily_trend_df):
    """
    Cria um gráfico de linha simples para mostrar a tendência de faturamento diário.
    É o modo mais básico de visualizar dados temporais.
    """
    plt.figure(figsize=(10, 5))
    
    # Plota a data no eixo X e o faturamento no eixo Y
    plt.plot(daily_trend_df['Date'], daily_trend_df['Daily_Revenue'])
    
    # Títulos e Rótulos (sem muita formatação)
    plt.title('Tendência de Faturamento Diário')
    plt.xlabel('Data da Transação')
    plt.ylabel('Faturamento Total (R$)')
    plt.grid(True) # Adiciona grid para facilitar a leitura dos valores
    
    plt.show() # Exibe o gráfico

# ---------------------------------------------------------------------- #

def get_best_selling_days(df):
    """
    Calcula o faturamento médio por dia da semana para identificar os dias mais fortes.
    
    Argumento:
        df (DataFrame): O DataFrame de vendas.
        
    Retorna:
        Series: Faturamento total por dia da semana, ordenado.
    """
    # 1. Extrai o nome do dia da semana (Ex: Monday, Tuesday)
    # A coluna já é datetime, usamos .dt para acessar os atributos de data/tempo
    df['Day_of_Week'] = df['transaction_date'].dt.day_name(locale='pt_BR') # 'pt_BR' para nomes em português

    # 2. Agrupa pelo dia da semana e soma o faturamento total
    sales_by_day = df.groupby('Day_of_Week')['Revenue'].sum()

    # Define a ordem correta dos dias da semana para exibir no gráfico
    # Sem isso, o Pandas ordena alfabeticamente (ex: Domingo antes de Segunda)
    days_order = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 
                  'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

    # 3. Reordena os resultados e pega o Top 3 para o insight
    sales_by_day_ordered = sales_by_day.reindex(days_order).fillna(0)
    top_3_days = sales_by_day_ordered.sort_values(ascending=False).head(3)
    
    # Micro-Insight Acionável
    print("\n🗓️ Insight de Dias da Semana:")
    print(f"O dia mais forte em faturamento é **{top_3_days.index[0]}**.")
    print(f"Os 3 dias mais fortes são:\n{top_3_days.to_string(float_format='R${:,.2f}'.format)}")
    
    return sales_by_day_ordered

# ---------------------------------------------------------------------- #

def plot_sales_by_day_of_week(sales_by_day_series):
    """
    Cria um gráfico de barras simples para comparar o faturamento por dia da semana.
    Usa os nomes dos dias da semana como rótulos.
    """
    plt.figure(figsize=(8, 5))
    
    # Cria o gráfico de barras diretamente da Series
    # O index (dias da semana) se torna o eixo X e os valores (Revenue) se tornam a altura das barras
    sales_by_day_series.plot(kind='bar', color='skyblue')
    
    plt.title('Faturamento Total por Dia da Semana')
    plt.xlabel('Dia da Semana')
    plt.ylabel('Faturamento Total (R$)')
    
    # Rotação dos rótulos para melhor leitura
    plt.xticks(rotation=45, ha='right') 
    
    plt.tight_layout() # Ajusta o layout para evitar cortes nos rótulos
    plt.show()

# ---------------------------------------------------------------------- #

def get_top_selling_products_qty(df, top_n=5):
    """
    Identifica os produtos mais vendidos com base na QUANTIDADE (transaction_qty).
    
    Argumentos:
        df (DataFrame): O DataFrame de vendas.
        top_n (int): Quantidade de produtos a serem listados.
        
    Retorna:
        DataFrame: Lista dos Top N produtos por quantidade.
    """
    # Agrupa pelo detalhe do produto e soma a quantidade transacionada (transaction_qty)
    top_products_qty = df.groupby('product_detail')['transaction_qty'].sum().reset_index()
    
    # Ordena de forma decrescente e seleciona os Top N
    top_products_qty_sorted = top_products_qty.sort_values(
        by='transaction_qty', ascending=False
    ).head(top_n)
    
    # Micro-Insight Acionável
    print(f"\n☕ Produtos Top {top_n} Mais Vendidos (Volume):")
    for index, row in top_products_qty_sorted.iterrows():
        print(f"   - {row['product_detail']}: {row['transaction_qty']} unidades vendidas.")
        
    print(f"\n💡 Micro-Insight: O produto de maior volume é **{top_products_qty_sorted.iloc[0]['product_detail']}**.")
    
    return top_products_qty_sorted

# ---------------------------------------------------------------------- #

def plot_top_selling_products(top_products_df):
    """
    Cria um gráfico de barras horizontais para mostrar os produtos mais vendidos por volume.
    Barras horizontais são boas para rótulos longos de nomes de produtos.
    """
    plt.figure(figsize=(8, 6))
    
    # Cria o gráfico de barras horizontais
    # Usamos Barras Horizontais ('barh') pois 'product_detail' pode ter nomes longos
    plt.barh(top_products_df['product_detail'], top_products_df['transaction_qty'], color='lightcoral')
    
    # Inverte o eixo Y para que o produto mais vendido fique no topo
    plt.gca().invert_yaxis() 
    
    plt.title('Top 5 Produtos por Quantidade Vendida')
    plt.xlabel('Quantidade Vendida (Unidades)')
    plt.ylabel('Produto')
    
    plt.show()

# ---------------------------------------------------------------------- #

df['Revenue'] = df['unit_price'] *  df['transaction_qty']

# Executar as análises
print("--------------------------------------------------")
daily_trend_df = get_daily_sales_trend(df.copy()) # .copy() para segurança
print("--------------------------------------------------")
best_days_series = get_best_selling_days(df.copy())
print("--------------------------------------------------")
top_qty_df = get_top_selling_products_qty(df.copy(), top_n=5)
print("--------------------------------------------------")

# Plotando os insights
print("--------------------------------------------------")
plot_sales_trend(daily_trend_df)
print("--------------------------------------------------")
plot_sales_by_day_of_week(best_days_series)
print("--------------------------------------------------")
plot_top_selling_products(top_qty_df)
print("--------------------------------------------------")