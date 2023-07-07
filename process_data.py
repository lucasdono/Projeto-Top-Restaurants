#ARQUIVO QUE SERÁ FEITO A LIMPEZA DOS DADOS

#bibliotecas requiridas
import pandas as pd
import numpy as np
import inflection

#ler csv
df = pd.read_csv('./data/raw/zomato.csv')

#checar valores NA
df.isna().sum()
df = df.dropna()


#RENOMEAÇÃO DE COLUNAS FEITAS PELO DS SENIOR
def rename_columns(dataframe):
  df = dataframe.copy()
  title = lambda x: inflection.titleize(x)
  snakecase = lambda x: inflection.underscore(x)
  spaces = lambda x: x.replace(" ", "")
  cols_old = list(df.columns)
  cols_old = list(map(title, cols_old))
  cols_old = list(map(spaces, cols_old))
  cols_new = list(map(snakecase, cols_old))
  df.columns = cols_new
  return df

df = rename_columns(df)


#PREENCHIMENTO DO NOME DOS PAISES FEITO PELO DS SENIOR
def country_name(country_id):
  COUNTRIES = {
  1: "India",
  14: "Australia",
  30: "Brazil",
  37: "Canada",
  94: "Indonesia",
  148: "New Zeland",
  162: "Philippines",
  166: "Qatar",
  184: "Singapure",
  189: "South Africa",
  191: "Sri Lanka",
  208: "Turkey",
  214: "United Arab Emirates",
  215: "England",
  216: "United States of America",
  }

  return COUNTRIES[country_id]


#Criação do Tipo de Categoria de Comida FEITA PELO DS SENIOR
def create_price_tye(price_range):
  if price_range == 1:
    return "cheap"
  elif price_range == 2:
    return "normal"
  elif price_range == 3:
    return "expensive"
  else:
    return "gourmet"


#CRIAÇÃO DO NOME DAS CORES CRIADO PELO DS SENIOR
def color_name(color_code):
  COLORS = {
  "3F7E00": "darkgreen",
  "5BA829": "green",
  "9ACD32": "lightgreen",
  "CDD614": "orange",
  "FFBA00": "red",
  "CBCBC8": "darkred",
  "FF7800": "darkred",
  }

  return COLORS[color_code]


#CATEGORIZAR TODOS OS RESTAURANTES POr UM TIPO DE CULINARIA
df['cuisines'] = df.loc[:, 'cuisines'].apply(lambda x: x.split(',')[0])
    
#ADICIONAR A COLUNA COUNTRY COM O NOME DOS PAISES DE ACORDO COM SEUS RESPECTIVOS CÓDIGOS
df["country"] = df.loc[:, "country_code"].apply(lambda x: country_name(x))

#adicionar a coluna color_name com os nomes de cada cor em seus respectivos códigos
df["color_name"] = df.loc[:, "rating_color"].apply(lambda x: color_name(x))

#excluir tipo de culinaria 'mineira' e 'drinks only', por deixar dados zerados

df = df.drop(df[(df["cuisines"] == "Drinks Only")].index)
df = df.drop(df[(df["cuisines"] == "Mineira")].index)

#excluir dados duplicados
df = df.drop_duplicates()


#EXPORTAR O DF PROCESSADO

df.to_csv('./data/processed/data.csv', index=False)




























































































      