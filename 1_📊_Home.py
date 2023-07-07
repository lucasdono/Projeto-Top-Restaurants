#BIBLIOTECAS NECESSARIAS
import pandas as pd #IMPORT DF
import folium #criar mapas
from folium.plugins import MarkerCluster #importar o comando de criar marcadores agrupados
import streamlit as st #acessar streamlit
from streamlit_folium import folium_static #importar comando para visualizar mapa no streamlit
from PIL import Image #usar imagem


#IMPORTAR DF
df = pd.read_csv('./data/processed/data.csv')



st.set_page_config(page_title= 'Main Home', layout = 'wide')
#----------------------------------------------------------------------
# SIDEBAR
#-------------------------------------------------------------------

image_path= './img/'
image = Image.open(image_path + 'logo_dx.png')

col1, col2 = st.sidebar.columns([1,2], gap='small') #

col1.image(image, width=130)
col2.markdown("# Fome Zero")

#filtro de pesquisa de dados
st.sidebar.markdown('## Filtros')
countries_select = st.sidebar.multiselect(
                    '##### Escolha os Paises que deseja visualizar os Restaurantes',
                    df.loc[:, 'country'].unique().tolist(), #comando usado para criar uma lista(tolist) de nomes unicos(unique) da coluna country
                    default = df.loc[:, 'country'].unique().tolist())


st.sidebar.markdown("""---""")


#botão de download

processed_data = pd.read_csv('./data/processed/data.csv')
st.sidebar.markdown('## Dados Tratados')
st.sidebar.download_button(
    'Download',
    data= processed_data.to_csv(index=False, sep=';'),
    file_name= 'data.csv',
    mime='text/csv')



#rodapé
st.sidebar.markdown("""---""")
st.sidebar.markdown('##### Powered by Lucas Donô - DS')




#----------------------------------------------------------------------
#  MAIN - tela principal
#---------------------------------------------------------------------
st.title('Fome Zero!')
st.markdown('## A forma mais simples para encontrar seu mais novo restaurante favorito!')


st.markdown('### Temos as seguintes marcas dentro da nossa plataforma:')

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(label = '### Restaurantes Registrados', 
            value=df['restaurant_id'].nunique())

col2.metric(label = '### Paises Cadastrados',
            value= df['country'].nunique())

col3.metric(label= '### Cidades cadastradas',
            value = df['city'].nunique())

col4.metric(label= '### Avaliações Feitas',
            value= f"{df['votes'].sum():,}".replace(',','.'))

col5.metric(label= '### Tipos de culinaria',
            value = df['cuisines'].nunique())



#MAPA
map_df = df.loc[df['country'].isin(countries_select), :]

f= folium.Figure(width=1920, height=1080) #cria uma figura (f), width e height são as dimensões da figura
m= folium.Map(max_bounds=True).add_to(f) #cria um mapa usando a figura (f) usando o .add_to / max_bounds=True define que o mapa será ajustado com todos os marcadores dentro do zoom que o usuario fizer
marker_cluster = MarkerCluster().add_to(m) #agrupa os marcadores no mapa, 'MarkerCluster' é adicionado ao mapa através do '.add_to(m)' assim permite que os marcadores sejam agrupados de acordo com zoom

for _, line in map_df.iterrows():   #percorre todas as linhas do df, sendo '_' para ignorar o index do df, 'line' as linhas do dd e .iterrows() interagir com todas as linhas, acessando seus valores

    #extrai os respectivos valores contidos em cada linha das colunas
    name = line["restaurant_name"]                
    price_for_two = line["average_cost_for_two"]
    cuisine = line["cuisines"]
    currency = line["currency"]
    rating = line["aggregate_rating"]
    color = f'{line["color_name"]}'


    #criar o popup interativo do mapa que ao clicar no restaurante da as seguintes informações

    #html cria os dados que serão visualizado no popup do folium (marcador do mapa)
    html = "<p><strong>{}</strong></p>" #<p> para escrever a string, </p> para finalizar a linha / <strong></strong> para transformar o texto em negrito / {} para introduzir o valor do .format no final
    html += "<p>Preço médio: {},00 ({}) para dois"
    html += "<br />Culinária: {}" #<br /> usado para quebrar a linha
    html += "<br />Avaliação média: {}/5.0"
    html = html.format(name, price_for_two, currency, cuisine, rating) #.format - usado para definir os valores que serão usados nos respectivos {} anteriores, lembrando que tem que estar em ordem

    #cria um objeto Popup do Folium, que é exibido quando o usuário clica em um marcador no mapa.
    popup = folium.Popup( #comando usado para criar o popup
            folium.Html(html, script=True), #comando usado para visualizar os dados que deseja mostrar no popup(marcador)
            max_width=500, #define o tamanho do popup em pixels no mapa
            )

    #adicionar marcadores
    folium.Marker( #comando para adicionar os marcadores no mapa
            [line["latitude"], line["longitude"]], #cria o marcador de acordo com a latitude e a longitude de cada linha percorrida
            popup=popup, #define o popup do marcador
            icon=folium.Icon(color=color, icon="home", prefix="fa"),#personaliza o icone dos marcadores, nesse caso usa a string com o nome da cor gerado através da variavel 'color' la em cima
                                                                    #icon="home" define o ícone como uma casa e prefix="fa" indica que o ícone é proveniente da biblioteca Font Awesome.
            ).add_to(marker_cluster)   #Adiciona o marcador ao objeto 'marker_cluster', que é um objeto que agrupa os marcadores no mapa e dissipa conforme da zoom. 

folium_static(m, width=1024, height=768) #exibe o mapa estatico 'm' e width/height define o tamanho que será exibido na tela













