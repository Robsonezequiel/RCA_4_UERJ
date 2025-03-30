#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose


#%%

file_path = r"C:\Users\robso\OneDrive\Área de Trabalho\UERJ_2025\1_Periodo\RCA_UERJ\chocolate_sales_excel.xlsx"
df = pd.read_excel(file_path)

#%%
#Distribuição de vendas por país: 
vendas_por_pais = df.groupby("Country")["Amount"].sum().sort_values(ascending=False)

#Criando um gráfico em barras
plt.figure(figsize=(10,5))
sns.barplot(x=vendas_por_pais.index, y=vendas_por_pais.values)
plt.xlabel("País")
plt.ylabel("Vendas")
plt.title("Distribuição de Vendas por País")
plt.show()

# %%
#Tipos de chocolates mais vendidos: 

tipo_chocolate = df.groupby("Product")["Amount"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=tipo_chocolate.values, y=tipo_chocolate.index, palette="magma")
plt.xlabel("Valor total vendido")
plt.ylabel("Produto")
plt.title("Tipos de chocolate mais vendido")
plt.show()

# %%
# Vendas por vendedor

media_vendedor = df.groupby("Sales Person")["Amount"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
media_vendedor.plot(kind="bar", figsize=(12,5), colormap="plasma")
plt.xlabel("Vendedor")
plt.ylabel("Média de vendas")
plt.show()
# %%
# Série temporal das vendas
df['Date'] = pd.to_datetime(df['Date'])

# Definindo a a data como indice:
df.set_index('Date', inplace=True)


# %%
plt.figure(figsize=(14,6))
sns.lineplot(x=df['Date'], y=df['Amount'])
plt.title("Valores ao longo do tempo")
plt.xlabel('Data')
plt.ylabel('Valores')
plt.show()

# %%
#Venda ao longo do tempo :


plt.figure(figsize=(14,6))
sns.lineplot(x=df['Date'], y=df['Boxes Shipped'])
plt.title("Vendas ao longo do tempo")
plt.xlabel('Data')
plt.ylabel('Boxes Shipped')
plt.show()

# %%
# Mapa de calor das vendas
mapa = df.pivot_table(
    index="Country",
    columns="Product",
    values="Amount",  # Coluna numérica!
    aggfunc="sum"
).fillna(0)

print(mapa)

#Criando Mapa: 
plt.figure(figsize=(20,18))
sns.heatmap(
    mapa,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu",
    linewidths=.5
    
    )

plt.title("Vendas por País e Produto", pad=20)
plt.xlabel("Produto")
plt.ylabel("País")
plt.tight_layout()
plt.show()

# %%

