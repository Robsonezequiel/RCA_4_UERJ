#%%
# 📊 Chocolate Sales - Análise Exploratória (EDA)
# Autor: Robson Ezequiel
# Versão: 1.1  
# Professora : Marina
# Objetivo:
# Explorar padrões de vendas, entender a distribuição dos dados e identificar relações entre variáveis.
# Principais Perguntas:
# Que tipo de chocolate é mais conusmido por pais ?
# Sanzonalidade das vendas e que época se consome mais ?
# Qual foi o vendedor com melhor desenpenho ? 
# Fonte dos dados: Kaggle
#%%
#Configurações: 
from heapq import nlargest
from operator import index
from turtle import color
from cv2 import rotate
from matplotlib import axis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from sqlalchemy import column 
import plotly.express as px
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6) # Padroniza o tamanho do gráfico

#%%
#Carregando o dataset: 

data_set_path = r"C:\Users\robso\OneDrive\Área de Trabalho\UERJ_2025\1_Periodo\RCA_UERJ\Chocolate_sales\data\chocolate_sales_excel.xlsx"
#%%
df = pd.read_excel(data_set_path)
# Visualização do dataset :
df.head(3).style.background_gradient(cmap="Blues")


#%%
# Verificando integridade dos dados: 
print("Metadados : ")
df.info(verbose=False)
# %%
# Verificando registro duplicado
print(f"Duplicados: {df.duplicated().sum()} Registros")

        
#%%
#Exploração dos dados:
df.shape
#%%
df.describe()

#%%
#
#%%
# Analise Univariada Vendedor
top_sellers = (
    df["Sales Person"]
    .value_counts()
    .nlargest(3)
    .rename_axis("Seller")
    .reset_index(name="Top Sellers")
    )

display(
    top_sellers.style
    .hide(axis="index")
    .bar(subset=["Top Sellers"], color="orange" )
    .set_caption("Top Sellers Performace")
)

print(top_sellers)


#%%
# Performace dos Vendedores
sns.countplot(y="Sales Person", data=df, order=df["Sales Person"].nlargest(3))
plt.title("Sellers Performance")
plt.xlabel("Sell Amount")
plt.ylabel("Sellers Name")
plt.show()


# %%
# Top Vendedores 
top_3 = (
    df.groupby("Sales Person")['Amount']
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

top_3.plot(kind='bar', color="Orange")
plt.title("Top Sellers")
plt.xlabel("Sellers Name")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#%%
# Produtos mais vendidos :
top_products = (
    df.groupby("Product")['Amount']
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

top_products.plot(kind='bar', color="green")
plt.title("Top Products")
plt.xlabel("Product Name")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#%%
# Produtos menos vendidos :
bottom_products = (
    df.groupby("Product")['Amount']
    .sum()
    .sort_values(ascending=True)
    .head(3)
)


bottom_products.plot(kind='bar', color="red")
plt.title("Bottom Products")
plt.xlabel("Product Name")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#%%
#Qual pais consome mais chocolate:

df["Amount"] = df["Amount"].replace(r'[\$,]', '', regex=True).astype(float) 

# Agregando venda por pais
df_country_sales = df.groupby("Country")["Amount"].sum().reset_index()

# Criando um mapa.
fig = px.choropleth(
    df_country_sales,
    locations="Country",           
    locationmode="country names", 
    color="Amount",                
    color_continuous_scale="Viridis",
    title="Total Sales by Country"
)

fig.show()




# %%
df.columns
# %%
