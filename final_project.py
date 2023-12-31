# -*- coding: utf-8 -*-
"""Final Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16_e_jhXV537kS7XAFc0oHyWNmR6xklmL

##Milestone 1 - Ilse & Lali

Goals:
 - Tell a story about data
 - Find the difference of exports and imports during a 10 year period in Luxembourg and look at any patterns, trends, and changes in trade flows over time.
 - Look at the data and see if countries have been getting more specialized in their exports and imports during time.
 - Compare the data from Luxembourg to other countries
 - Create a dashboard using Manganite

Milestone 1:
- Clean Luxembourg data
- Create graphs for Luxembourg imports and exports

Milestone 2:
- Clean data for Germany, Belgium, France and Netherlands
- Compare Luxembourg's exports and imports against the mentioned countries for all categories during the 10 year period.
- Choose one specific category to focus and make a detailed comparison.
"""

import pandas as pd
import polars as pl
import plotly.express as px
import csv
import plotly.io as pio
pio.templates.default = 'plotly_white'
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

"""# What did Luxembourg export between 2010 and 2020"""

url = "https://www.dl.dropboxusercontent.com/scl/fi/vkwffpdw6rvlxug3einxc/Luxembourg-export-between-2010-and-2020.csv?rlkey=2jfcgis7vbovlkr9srxzkm5cj&dl=1"

df_1 = pd.read_csv(url)

df_1 = df_1.drop('Code', axis=1)
df_1 = df_1.rename(columns={'Current Gross Export': 'Gross Export in USD'})
df_1['Gross Export in USD'] = df_1['Gross Export in USD'].str.replace("$", "")
df_1['Gross Export in USD'] = df_1['Gross Export in USD'].str.replace('M', 'e6').str.replace('B', 'e9')
df_1['Gross Export in USD'] = pd.to_numeric(df_1['Gross Export in USD'], errors='coerce').astype('Int64')


display(df_1)

df_1.info()

df_1 = df_1.sort_values(by="Year")
df_1

fig = px.line(df_1, x="Year", y="Gross Export in USD", color="Sector")
fig.show()

"""#What did Luxembourg import between 2010 and 2020"""

url = "https://www.dropbox.com/scl/fi/9dzw3h28263fjirgr7fyj/What-did-Luxembourg-import-between-2010-and-2020_.csv?rlkey=xui2dv36smy3jnh7kaklsqupp&dl=1"

df_2 = (pd.read_csv(url)
        .drop('Code', axis=1)
        .rename(columns={'Current Gross Import': 'Gross Import in USD'})
        .assign(**{'Gross Import in USD': lambda x: x['Gross Import in USD'].str.replace("$", "")
        .str.replace('M', 'e6')
        .str.replace('B', 'e9')})
        .assign(**{'Gross Import in USD': lambda x: pd.to_numeric(x['Gross Import in USD'], errors='coerce').astype('Int64')})
       )

display(df_2)

fig = px.line(df_2, x="Year", y="Gross Import in USD", color="Sector")
fig.show()

df_2.info()

df_2 = df_2.sort_values(by="Year")
df_2

"""#Add Exports and Imports in just one table"""

Gross_Import = df_2['Gross Import in USD']
df_1['Gross Import in USD'] = Gross_Import

df_1

df_1.describe()

fig = px.line(df_1, x="Year", y=["Gross Export in USD", "Gross Import in USD"], color="Sector")
fig.show()

fig = px.bar(df_1.sort_values(["Gross Export in USD"]), x="Gross Export in USD", y="Year", color="Sector",orientation="h")
fig.show()

fig_2 = px.bar(df_1.sort_values(["Gross Import in USD"]),y="Year", x="Gross Import in USD", color="Sector", orientation="h")
fig_2.show()

"""#Exports and imports of Germany from 2010 to 2020"""

germany_ex = "https://www.dropbox.com/scl/fi/rr9us1t56k9gpon0zpcuy/What-did-Germany-export-between-2010-and-2020_.csv?rlkey=538pc7805vz7xcz0iwrxt1ly6&dl=1"
df_GE = (pd.read_csv(germany_ex)
        .drop('Code', axis=1)
        .rename(columns={'Current Gross Export': 'Gross Export in USD'})
        .assign(**{'Gross Export in USD': lambda x: x['Gross Export in USD'].str.replace("$", "")
        .str.replace('M', 'e6')
        .str.replace('B', 'e9')})
        .assign(**{'Gross Export in USD': lambda x: pd.to_numeric(x['Gross Export in USD'], errors='coerce').astype('Int64')})
        .sort_values(by="Year")
       )

germany_im = "https://www.dropbox.com/scl/fi/lzhrmgy292ow349llipyb/What-did-Germany-import-between-2010-and-2020_.csv?rlkey=w3m2k2qho257llrw4jon7wgp8&dl=1"
df_GI = (pd.read_csv(germany_im)
        .drop('Code', axis=1)
        .rename(columns={'Current Gross Import': 'Gross Import in USD'})
        .assign(**{'Gross Import in USD': lambda x: x['Gross Import in USD'].str.replace("$", "")
        .str.replace('M', 'e6')
        .str.replace('B', 'e9')})
        .assign(**{'Gross Import in USD': lambda x: pd.to_numeric(x['Gross Import in USD'], errors='coerce').astype('Int64')})
        .sort_values(by="Year")
       )

Gross_Import_Germany = df_GI['Gross Import in USD']
df_GE['Gross Import in USD'] = Gross_Import_Germany

df_GE

fig = px.line(df_GE, x="Year", y='Gross Export in USD', color="Sector")
fig.show()

fig = px.line(df_GE, x="Year", y='Gross Import in USD', color="Sector")
fig.show()

fig_GE = px.treemap(df_GE,
                   path=["Year", "Sector"],
                   values="Gross Export in USD",
                   color="Sector")
fig_GE.show()

"""#Exports and imports of Belgium from 2010 to 2020


"""

belgium_ex = "https://www.dropbox.com/scl/fi/awy9lm0fyku4wp6uva9x8/What-did-Belgium-export-between-2010-and-2020_.csv?rlkey=oq2tvqetjs962fhtxj8erfk6f&dl=1"
df_BE = (pd.read_csv(belgium_ex)
        .drop('Code', axis=1)
        .rename(columns={'Current Gross Export': 'Gross Export in USD'})
        .assign(**{'Gross Export in USD': lambda x: x['Gross Export in USD'].str.replace("$", "")
        .str.replace('M', 'e6')
        .str.replace('B', 'e9')})
        .assign(**{'Gross Export in USD': lambda x: pd.to_numeric(x['Gross Export in USD'], errors='coerce').astype('Int64')})
        .sort_values(by="Year")
       )

belgium_im = "https://www.dropbox.com/scl/fi/b80a2sq5khlrnymheuab0/What-did-Belgium-import-between-2010-and-2020_.csv?rlkey=h83q5irax243zh7i8307kn3nv&dl=1"
df_BI = (pd.read_csv(belgium_im)
        .drop('Code', axis=1)
        .rename(columns={'Current Gross Import': 'Gross Import in USD'})
        .assign(**{'Gross Import in USD': lambda x: x['Gross Import in USD'].str.replace("$", "")
        .str.replace('M', 'e6')
        .str.replace('B', 'e9')})
        .assign(**{'Gross Import in USD': lambda x: pd.to_numeric(x['Gross Import in USD'], errors='coerce').astype('Int64')})
        .sort_values(by="Year")
       )

Gross_Import_Belgium = df_BI['Gross Import in USD']
df_BE['Gross Import in USD'] = Gross_Import_Belgium

df_BE

fig = px.line(df_BE, x="Year", y='Gross Export in USD', color="Sector")
fig.show()

fig = px.line(df_BE, x="Year", y='Gross Import in USD', color="Sector")
fig.show()

"""#Exports and imports of France from 2010 to 2020


"""

france_ex = "https://www.dropbox.com/scl/fi/1nuqy9zopphf9ux47gte5/What-did-France-export-between-2010-and-2020_.csv?rlkey=eh80wedkkmt7my91mqdb44eic&dl=1"
df_FE = (pd.read_csv(france_ex)
        .drop('Code', axis=1)
        .rename(columns={'Current Gross Export': 'Gross Export in USD'})
        .assign(**{'Gross Export in USD': lambda x: x['Gross Export in USD'].str.replace("$", "")
        .str.replace('M', 'e6')
        .str.replace('B', 'e9')})
        .assign(**{'Gross Export in USD': lambda x: pd.to_numeric(x['Gross Export in USD'], errors='coerce').astype('Int64')})
        .sort_values(by="Year")
       )

france_im = "https://www.dropbox.com/scl/fi/d398r1kov1zwcub5h901i/What-did-France-import-between-2010-and-2020_.csv?rlkey=gq1vrs28ucod3lv4sg9f6letc&dl=1"
df_FI = (pd.read_csv(france_im)
        .drop('Code', axis=1)
        .rename(columns={'Current Gross Import': 'Gross Import in USD'})
        .assign(**{'Gross Import in USD': lambda x: x['Gross Import in USD'].str.replace("$", "")
        .str.replace('M', 'e6')
        .str.replace('B', 'e9')})
        .assign(**{'Gross Import in USD': lambda x: pd.to_numeric(x['Gross Import in USD'], errors='coerce').astype('Int64')})
        .sort_values(by="Year")
       )

Gross_Import_France = df_FI['Gross Import in USD']
df_FE['Gross Import in USD'] = Gross_Import_France

df_FE

fig = px.line(df_FE, x="Year", y='Gross Export in USD', color="Sector")
fig.show()

fig = px.line(df_FE, x="Year", y='Gross Import in USD', color="Sector")
fig.show()

"""#Exports and imports of Netherlands from 2010 to 2020"""

netherlands_ex ='https://www.dropbox.com/scl/fi/xucwu4nufbt9n7hsg3v5g/What-did-Netherlands-export-between-2010-and-2020_.csv?rlkey=1j2xlopy3a52vznca87gwldxl&dl=1'

df_NE = (pd.read_csv(netherlands_ex)
        .drop('Code', axis=1)
        .rename(columns={'Current Gross Export': 'Gross Export in USD'})
        .assign(**{'Gross Export in USD': lambda x: x['Gross Export in USD'].str.replace("$", "")
        .str.replace('M', 'e6')
        .str.replace('B', 'e9')})
        .assign(**{'Gross Export in USD': lambda x: pd.to_numeric(x['Gross Export in USD'], errors='coerce').astype('Int64')})
        .sort_values(by="Year")
       )

netherlands_im = "https://www.dropbox.com/scl/fi/tagwodgvgb1vhpkgfxke9/What-did-Netherlands-import-between-2010-and-2020_.csv?rlkey=i6hw12orixqz5j80yzjle5x5d&dl=1"
df_NI = (pd.read_csv(netherlands_im)
        .drop('Code', axis=1)
        .rename(columns={'Current Gross Import': 'Gross Import in USD'})
        .assign(**{'Gross Import in USD': lambda x: x['Gross Import in USD'].str.replace("$", "")
        .str.replace('M', 'e6')
        .str.replace('B', 'e9')})
        .assign(**{'Gross Import in USD': lambda x: pd.to_numeric(x['Gross Import in USD'], errors='coerce').astype('Int64')})
        .sort_values(by="Year")
       )

Gross_Import_Netherlands = df_NI['Gross Import in USD']
df_NE['Gross Import in USD'] = Gross_Import_Netherlands

df_NE

#Add tree map all the countries for 2020