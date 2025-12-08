import pandas as pd
import matplotlib.pyplot as plt

FILEPATH = 'data/Coffee Shop Sales.xlsx'

# ------------------------- #
# Leitura e preparação
# ------------------------- #

df = pd.read_excel(FILEPATH)
df['Revenue'] = df['unit_price'] * df['transaction_qty']
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# ------------------------- #
# Funções de análise
# ------------------------- #

def daily_sales(df):
    """ Retorna faturamento total por dia. """
    return (
        df.groupby('transaction_date')['Revenue']
        .sum()
        .reset_index(name='Daily_Revenue')
    )

def sales_by_weekday(df):
    """ Retorna faturamento total por dia da semana. """
    df['weekday'] = df['transaction_date'].dt.day_name()
    order = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
    result = df.groupby('weekday')['Revenue'].sum()
    return result.reindex(order)

def top_products(df, n=5):
    """ Retorna top N produtos por volume vendido. """
    return (
        df.groupby('product_detail')['transaction_qty']
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

# ------------------------- #
# Funções de visualização
# ------------------------- #

def plot_daily_sales(trend):
    plt.figure(figsize=(10,4))
    plt.plot(trend['transaction_date'], trend['Daily_Revenue'])
    plt.title('Tendência de Faturamento Diário')
    plt.xlabel('Data')
    plt.ylabel('Faturamento (R$)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_weekday_sales(weekday):
    plt.figure(figsize=(8,4))
    weekday.plot(kind='bar')
    plt.title('Faturamento por Dia da Semana')
    plt.xlabel('Dia')
    plt.ylabel('Faturamento (R$)')
    plt.tight_layout()
    plt.show()

def plot_top_products(df_top):
    plt.figure(figsize=(8,4))
    plt.barh(df_top['product_detail'], df_top['transaction_qty'])
    plt.gca().invert_yaxis()
    plt.title('Top Produtos por Volume')
    plt.xlabel('Unidades Vendidas')
    plt.tight_layout()
    plt.show()

# ------------------------- #
# Execução
# ------------------------- #

daily = daily_sales(df)
weekday = sales_by_weekday(df)
top = top_products(df, n=5)

plot_daily_sales(daily)
plot_weekday_sales(weekday)
plot_top_products(top)
