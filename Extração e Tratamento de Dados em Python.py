# -*- coding: utf-8 -*-
"""RID185846_Desafio05.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dL4_oeXSHzgrqAcfv71a51czWwmJefA_

# **Etapa 01) Leia o arquivo e inspecione os dados**
"""

from google.colab import files
upload = files.upload()

import pandas as pd
import numpy as np

df = pd.read_csv("data.csv", encoding='latin-1')

df.head()

df.describe()

"""# **Etapa 02) Valores faltantes na identificação do cliente**"""

df.info()

df.isna().sum()

df.dropna(subset=['CustomerID'], inplace=True)

df.info()

df.isna().sum()

"""# **Etapa 03) Preços unitários e quantidade de produtos iguais ou inferior a 0**"""

df.isna().sum()

df[df["UnitPrice"]<=0]

df[df["Quantity"]<=0]

df.drop(df[df["UnitPrice"]<=0].index, inplace=True)
df.drop(df[df["Quantity"]<=0].index, inplace=True)

df.info()

"""# **Etapa 04) Verifique se existem linhas duplicadas**"""

df[df.duplicated(keep=False)]

df.drop_duplicates(inplace=True)

df.info()

"""# **Etapa 05) Tipos de dados da coluna**"""

df.dtypes

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["CustomerID"] = df["CustomerID"].astype(int)

df.info()

"""# **Etapa 06) Tratando os outliers**"""

df.plot.box();

df[df["Quantity"]>10000]

df[df["UnitPrice"]>5000]

df.drop(df[df["UnitPrice"]>10000].index, inplace=True)
df.drop(df[df["Quantity"]>5000].index, inplace=True)

df.plot.box();

"""# **Etapa 07) Crie uma coluna adicional**"""

df.head()

df["preço_total"] = df["UnitPrice"] * df["Quantity"]

df.head()

df.info()

"""# **Etapa 08) Última data**"""

df.groupby("CustomerID")["InvoiceDate"].max().sort_values(ascending=False)

data = df["InvoiceDate"].max()
print(data)

"""# **Etapa 09) Plotando gráficos**"""

import matplotlib.pyplot as plt

top10paises = df.groupby(["Country"])["preço_total"].sum().sort_values(ascending=False).head(10)
top10paises

top10produtos = df.groupby(["Description"])["preço_total"].sum().sort_values(ascending=False).head(10)
top10produtos

vendasMes = df.groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasMes

vendasUK = df[df["Country"]=="United Kingdom"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasUK

vendasHolanda = df[df["Country"]=="Netherlands"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasHolanda

vendasIrlanda = df[df["Country"]=="EIRE"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasIrlanda

vendasAlemanha = df[df["Country"]=="Germany"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasAlemanha

vendasFranca = df[df["Country"]=="France"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasFranca

vendasAustralia = df[df["Country"]=="Australia"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasAustralia

vendasEspanha = df[df["Country"]=="Spain"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasEspanha

vendasSuica = df[df["Country"]=="Switzerland"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasSuica

vendasBelgica = df[df["Country"]=="Belgium"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasBelgica

vendasSuecia = df[df["Country"]=="Sweden"].groupby(df["InvoiceDate"].dt.month)["preço_total"].sum()
vendasSuecia

fig = plt.figure(figsize=(20,5))
plt.bar(top10paises.index, top10paises.values, color="lightskyblue")
plt.title("Top 10 países com maior valor em vendas", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(top10produtos.index, top10produtos.values, color="lightskyblue")
plt.title("Top 10 produtos mais vendidos", loc="center", fontsize=18, fontweight="bold", color="black");
plt.xticks(rotation=90);

fig = plt.figure(figsize=(20,5))
plt.bar(vendasMes.index, vendasMes.values, color="lightskyblue")
plt.title("Valor de venda total por mês", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasUK.index, vendasUK.values, color="lightskyblue")
plt.title("Valor de venda total por mês em United Kingdom", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasHolanda.index, vendasHolanda.values, color="lightskyblue")
plt.title("Valor de venda total por mês em Netherlands", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasIrlanda.index, vendasIrlanda.values, color="lightskyblue")
plt.title("Valor de venda total por mês em EIRE", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasAlemanha.index, vendasAlemanha.values, color="lightskyblue")
plt.title("Valor de venda total por mês em Germany", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasFranca.index, vendasFranca.values, color="lightskyblue")
plt.title("Valor de venda total por mês em France", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasAustralia.index, vendasAustralia.values, color="lightskyblue")
plt.title("Valor de venda total por mês em Australia", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasEspanha.index, vendasEspanha.values, color="lightskyblue")
plt.title("Valor de venda total por mês em Spain", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasSuica.index, vendasSuica.values, color="lightskyblue")
plt.title("Valor de venda total por mês em Switzerland", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasBelgica.index, vendasBelgica.values, color="lightskyblue")
plt.title("Valor de venda total por mês em Belgium", loc="center", fontsize=18, fontweight="bold", color="black");

fig = plt.figure(figsize=(20,5))
plt.bar(vendasSuecia.index, vendasSuecia.values, color="lightskyblue")
plt.title("Valor de venda total por mês em Sweden", loc="center", fontsize=18, fontweight="bold", color="black");

"""# **Etapa 10) Cálculo do RFM**"""

RFM = df.groupby("CustomerID").agg({"InvoiceDate": lambda x: (data - x.max()).days,
                                     "InvoiceNo": lambda x: len(x),
                                     "preço_total": lambda x: x.sum()})
RFM

