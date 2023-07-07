#BIBLIOTECAS NECESSARIAS
import pandas as pd #IMPORT DF
import folium #criar mapas
import streamlit as st #acessar streamlit
from PIL import Image #usar imagem
import plotly.express as px

#IMPORTAR DF
df = pd.read_csv('./data/processed/data.csv')


st.set_page_config(page_title="Cities", layout="wide")

#----------------------------------------------------------------------
# SIDEBAR
#-------------------------------------------------------------------


#filtro de pesquisa de dados
st.sidebar.markdown('## Filtros')
country_options = st.sidebar.multiselect(
    '##### Escolha os Paises que deseja visualizar os Restaurantes',
    df.loc[:, 'country'].unique().tolist(), #comando usado para criar uma lista(tolist) de nomes unicos(unique) da coluna country
    default = df.loc[:, 'country'].unique().tolist())

linhas = df['country'].isin(country_options)
df = df.loc[linhas, :]


#rodapé
st.sidebar.markdown("""---""")
st.sidebar.markdown('##### Powered by Lucas Donô - DS')


#---------------------------------------------------------------------
#  MAIN
#--------------------------------------------------------------------

st.title(' 🏙️ Visão Cidades')

#top 10 cidades com mais restaurantes na base de dados
df_aux = df.loc[:, ['city', 'restaurant_id','country']].groupby(['city', 'country']).nunique('restaurant_id').sort_values('restaurant_id', ascending=False).reset_index()
fig = px.bar(df_aux.head(10),
             x='city',
             y='restaurant_id',
             title='Top 10 Cidades com mais Restaurantes na Base de Dados',
             text='restaurant_id',
             color='country',
             text_auto='.2f',
             labels={'city': 'Cidade',
                     'restaurant_id': 'Quantidade de Restaurantes',
                     'country': 'Países'})

st.plotly_chart(fig, use_container_width=True)


#top 7 cidades com restaurantes com média de avaliação acima de 4 / top 7 cidades com restaurantes com média de avaliação abaixo de 2,5
col1, col2 = st.columns(2)

with col1:
    linhas = df['aggregate_rating'] >= 4
    cols = ['city', 'restaurant_id','country']

    df_aux = df.loc[linhas, cols].groupby(['city', 'country']).nunique('restaurant_id').sort_values('restaurant_id', ascending=False).reset_index()
    fig = px.bar(df_aux.head(7),
                 x='city',
                 y='restaurant_id',
                 title='Top 7 Cidades com Restaurantes com média de avaliação acima de 4',
                 text='restaurant_id',
                 text_auto='.2f',
                 color='country',
                 labels={'city':'Cidade',
                         'restaurant_id':'Quantidade de Restaurantes',
                         'country': 'Países'})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    linhas = df['aggregate_rating'] <= 2.5
    cols = ['city', 'restaurant_id','country']

    df_aux = df.loc[linhas, cols].groupby(['country', 'city']).nunique('restaurant_id').sort_values('restaurant_id', ascending=False).reset_index()
    fig = px.bar(df_aux.head(7),
                 x='city',
                 y='restaurant_id',
                 title='Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5',
                 text='restaurant_id',
                 text_auto='.2f',
                 color='country',
                 labels={'city':'Cidade',
                         'restaurant_id':'Quantidade de Restaurantes',
                         'country': 'Países'})
    st.plotly_chart(fig, use_container_width=True)


#top 10 cidades mais restaurantesa com tipos de culinarias distintas
df_aux = df.loc[:, ['city', 'cuisines','country']].groupby(['country', 'city']).nunique().sort_values('cuisines', ascending = False).reset_index()
fig= px.bar(df_aux.head(10),
            x='city',
            y='cuisines',
            title='Top 10 Cidades com Restaurantes com mais Tipos Culinários Distintos',
            text='cuisines',
            text_auto='.2f',
            color='country',
            labels={'city':'Cidade',
                    'cuisines':'Quantidade de Tipos Culinários Únicos',
                    'country' : 'Países'})

st.plotly_chart(fig, use_container_width=True)
            


