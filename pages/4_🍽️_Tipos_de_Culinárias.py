#BIBLIOTECAS NECESSARIAS
import pandas as pd #IMPORT DF
import folium #criar mapas
import streamlit as st #acessar streamlit
from PIL import Image #usar imagem
import plotly.express as px


#IMPORTAR DF
df = pd.read_csv('./data/processed/data.csv')
              


st.set_page_config(page_title="Cousines", layout="wide")
#----------------------------------------------------------------------
# SIDEBAR
#-------------------------------------------------------------------


#filtro de pesquisa de dados
st.sidebar.markdown('## Filtros')
countries_select = st.sidebar.multiselect(
    '##### Escolha os Paises que deseja visualizar os Restaurantes',
    df.loc[:, 'country'].unique().tolist(), #comando usado para criar uma lista(tolist) de nomes unicos(unique) da coluna country
    default = df.loc[:, 'country'].unique().tolist())

st.sidebar.markdown("""---""")


#filtro de quantidade de restaurantes que deseja visualizar
top = st.sidebar.slider(
        'Selecione a Quantidade de Restaurantes que deseja visualizar',
        value = 10,
        min_value= 1,
        max_value= 20)

st.sidebar.markdown("""---""")


#filtro escolha tipos de culinaria
cuisines_type = st.sidebar.multiselect(
            '#### Escolha os Tipos de Culinaria',
            df.loc[:, 'cuisines'].unique().tolist(),
            default = ['Italian', 'Home-made', 'BBQ', 'Brazilian', 'Japanese'])


#rodapé
st.sidebar.markdown("""---""")
st.sidebar.markdown('##### Powered by Lucas Donô - DS')

#---------------------------------------------------------------------
#  MAIN
#--------------------------------------------------------------------
#FUNÇÃO PARA METRIC DE MELHORES RESTAURANTES DOS PRINCIPAIS TIPOS CULINARIOS
def metric(cuisines, top):

  cols = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes",
    ]

  linhas = df['cuisines'] == cuisines
  resultado = df.loc[linhas, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[top,True]).iloc[0,:].to_dict()


  return resultado


def display_metric(cuisines, top):
    result = metric(cuisines, top)
    
    label = f'{cuisines}: {result["restaurant_name"]}'
    value = f'{result["aggregate_rating"]}/5.0'
    help= f'''
          País: {result["country"]}\n
          Cidade: {result["city"]}\n
          Preço Médio do Prato para Dois: {result["average_cost_for_two"]} {result["currency"]}
          '''
    
    st.metric(label=label, value=value, help=help)
    return None


#colunas para os dados
cols = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes",
    ]



#titulo
st.title(' 🍽️ Visão Tipos de Culinária')

st.markdown('## Melhores Restaurantes dos principais tipos Culinarios')
italian, american, arabian, japanese, brazilian = st.columns(5)

with italian:
    metric('Italian', False)
    display_metric('Italian', False)

    
with american:
    metric('Italian', False)
    display_metric('American', False)
    
    

with arabian:
    metric('Arabian', False)
    display_metric('Arabian',False) 
   

with japanese:
    metric('Japanese', False)
    display_metric('Japanese',False) 
   


with brazilian:
    metric('Brazilian', False)
    display_metric('Brazilian',False) 
    

    

st.markdown("""---""")

#df com top restaurantes
st.title(f"Top {top} Restaurantes")
lines = (df['cuisines'].isin(cuisines_type)) & (df['country'].isin(countries_select))
df_aux = df.loc[lines, cols].sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True]).head(top)
df_aux
            
st.markdown("""---""")


#top melhores tipos de culinarias / top piores tipos de culinarias

col1, col2 = st.columns(2)

with col1:
    linhas = df['country'].isin(countries_select)
    df_aux = df.loc[linhas, ['cuisines', 'aggregate_rating']].groupby('cuisines').mean().sort_values('aggregate_rating', ascending=False).reset_index().head(top)
    fig = px.bar(df_aux.head(top), 
                 x='cuisines',
                 y='aggregate_rating',
                 title=f"Top {top} Piores Tipos de Culinárias",
                 text='aggregate_rating',
                 text_auto='.2f',
                 labels={'cuisines': 'Tipo de Culinária',
                        'aggregate_rating': 'Média de Avaliação Média'})
    st.plotly_chart(fig, use_container_witdh=True)

with col2:
    linhas = (df['country'].isin(countries_select) & (df['cuisines'] != 'Mineira') & (df['cuisines'] != 'Drinks Only')) #removido mineira e drinks only por estarem zerados
    df_aux = df.loc[linhas, ['cuisines', 'aggregate_rating']].groupby('cuisines').mean().sort_values('aggregate_rating', ascending=True).reset_index().head(top)
    fig = px.bar(df_aux.head(top), 
                 x='cuisines',
                 y='aggregate_rating',
                 title=f"Top {top} Piores Tipos de Culinárias",
                 text='aggregate_rating',
                 text_auto='.2f',
                 labels={'cuisines': 'Tipo de Culinária',
                        'aggregate_rating': 'Média de Avaliação Média'})
    st.plotly_chart(fig, use_container_witdh=True)
    














