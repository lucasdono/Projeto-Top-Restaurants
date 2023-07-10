#BIBLIOTECAS NECESSARIAS
import pandas as pd #IMPORT DF
import folium #criar mapas
import streamlit as st #acessar streamlit
from PIL import Image #usar imagem
import plotly.express as px


#IMPORTAR DF
df = pd.read_csv('./data/processed/data.csv')

st.set_page_config(page_title="Countries", layout="wide")

#----------------------------------------------------------------------
# SIDEBAR
#-------------------------------------------------------------------


#filtro de pesquisa de dados
st.sidebar.markdown('## Filtros')
country_options = st.sidebar.multiselect(
    'Escolha os Paises que deseja visualizar os Restaurantes',
    df.loc[:, 'country'].unique().tolist(), #comando usado para criar uma lista(tolist) de nomes unicos(unique) da coluna country
    default = df.loc[:, 'country'].unique().tolist())

linhas = df['country'].isin(country_options)
df = df.loc[linhas,:]


#rodapé
st.sidebar.markdown("""---""")
st.sidebar.markdown('##### Powered by Lucas Donô - DS')


#---------------------------------------------------------------------
#  MAIN
#--------------------------------------------------------------------
st.title(' 🌍 Visão Países')
#QUANTIDADE DE CIDADES RESGISTRADAS

df_aux = (df.loc[:, ['country', 'city']]
            .groupby('country')
            .nunique('city')
            .sort_values('city', ascending = False)
            .reset_index())

fig= px.bar(df_aux, 
            x='country', 
            y='city',
            text='city', #dado inserido dentro da barra
            title = 'Quantidade de Cidades Registradas por País',
            labels={'country' : 'Paises',
                    'city': ' Quantidade de Cidades'})
st.plotly_chart(fig, use_container_width=True)


#QUANTIDADE DE RESTAURANTES REGISTRADOS
df_aux = (df.loc[: , ['country', 'restaurant_id']]
            .groupby('country')
            .nunique('restaurant_id')
            .reset_index()
            .sort_values('restaurant_id', ascending=False))

fig= px.bar(df_aux,
             x='country',
             y='restaurant_id',
             text='restaurant_id',
             title='Quantidade de Restaurantes Registrados por País',
             labels={'country': 'Paises',
                     'restaurant_id': 'Restaurantes'})
st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns(2)

with col1:
    #média de avaliação feitas por país
    df_aux = (df.loc[:, ['country', 'votes']]
                .groupby('country')
                .mean('votes')
                .reset_index()
                .sort_values('votes', ascending=False))
    fig = px.bar(df_aux,
                 x='country',
                 y='votes',
                 text='votes',
                 text_auto='.2f', #formatação para 2 casas decimais apenas
                 title='Média de Avaliação Feita Por País',
                 labels={'country': 'Paises',
                         'votes': 'Quantidade de Avaliaçôes'})
    st.plotly_chart(fig, use_container_width=True)


with col2:
    #média de preço de um prato para duas pessoas por país
    df_aux = (df.loc[:, ['country', 'average_cost_for_two']]
                .groupby('country')
                .mean()
                .reset_index()
                .sort_values('average_cost_for_two', ascending=False))
    fig = px.bar(df_aux,
                 x='country',
                 y='average_cost_for_two',
                 text='average_cost_for_two',
                 text_auto='.2f',
                 title='Média de Preço de um Prato para Duas Pessoas',
                 labels={'country': 'Paises',
                         'average_cost_for_two': 'Preço do Prato para duas Pessoas'})
    st.plotly_chart(fig, use_container_width=True)
                 





          
