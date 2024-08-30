#==================================================================
# Libraries
#==================================================================
import pandas as pd
import inflection
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from PIL import Image
from streamlit_folium import folium_static

#==================================================================
# Import e cópia do dataset
#==================================================================
df = pd.read_csv('dataset/zomato.csv')
df1 = df.copy()

#==================================================================
# Limpeza e funções aplicadas em todo o projeto
#==================================================================
df1 = df1.drop_duplicates() # Deletando valores duplicados
df1 = df1.loc[(df1['Cuisines'].notnull()) , :] # Deletando valores nulos de 'Cuisines'

#======== Ajustes nos países ========#
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
    216: "United States of America"
}
def country_name(country_id):
    return COUNTRIES[country_id] # Dicionáriocom os códigos dos países

df1['Country Code'] = df1['Country Code'].map(COUNTRIES) # Trocando os códigos pelo nome dos países

df1.rename(columns={'Country Code': 'Country Name'}, inplace=True) # Renomeando a coluna dos países

#======== Ajustes nos nomes das colunas ========#
def rename_columns(dataframe):
    df1 = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df1.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df1.columns = cols_new
    
    return df1 # Padronizar o nome das colunas do DataFrame

df1 = rename_columns(df1) # Aplicar o novo nome nas colunas

df1.drop(['address', 'locality', 'locality_verbose', 'rating_text', 'switch_to_order_menu'], axis=1, inplace=True) # Apagar as colunas que não serão usadas nas análises

#======== Ajustes na coluna de tipo de culinária ========#
df1['cuisines'] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0]) # Deixando apenas um tipo de cozinha por registro

#======== Ajustes na coluna do range de preço ========#
def create_price_tye(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet" # Criação do Tipo de Categoria de Comida

#======== Ajustes na coluna das cores ========#
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred"
}
def color_name(color_code):
    return COLORS[color_code] # Criação do nome das Cores

df1['color_name'] = df1['rating_color'].map(COLORS) # Criando coluna com nome das cores para usar no mapa

#======== Reset do Index ========#
df1.reset_index(inplace=True, drop=True)

#======== Outlier ========#
df1.loc[356, 'average_cost_for_two'] = 250 # Substituindo um valor outlier na Australia

#======== Ajustando a coluna de preço médio para duas pessoas ========#
def currency_to_dollar(average_cost_for_two, currency):
    if currency == 'Botswana Pula(P)':
        return average_cost_for_two * 0.0748
    elif currency == 'Brazilian Real(R$)':
        return average_cost_for_two * 0.1830
    elif currency == 'Emirati Diram(AED)':
        return average_cost_for_two * 0.2722
    elif currency == 'Indian Rupees(Rs.)':
        return average_cost_for_two * 0.01190
    elif currency == 'Indonesian Rupiah(IDR)':
        return average_cost_for_two * 0.000065
    elif currency == 'NewZealand($)':
        return average_cost_for_two * 0.6232
    elif currency == 'Pounds(£)':
        return average_cost_for_two * 1.3209
    elif currency == 'Qatari Rial(QR)':
        return average_cost_for_two * 0.2742
    elif currency == 'Rand(R)':
        return average_cost_for_two * 0.5638
    elif currency == 'Sri Lankan Rupee(LKR)':
        return average_cost_for_two * 0.003333
    elif currency == 'Turkish Lira(TL)':
        return average_cost_for_two * 0.0294
    else:
        return average_cost_for_two # Função para converter os valores para USD com base na cotação de 24/08/2024
    
df1['average_cost_in_usd'] = df1.apply(lambda row: currency_to_dollar(row['average_cost_for_two'], row['currency']), axis=1) # Criando coluna com valores para dois em USD

df1.drop(['currency', 'average_cost_for_two'], axis=1, inplace=True) # Retirando as colunas 'currency' e 'average_cost_for_two'

#==================================================================
# Funções - Cities Page
#==================================================================

# Função para plotar o gráfico com as 10 cidades com mais restaurantes
def count_rest_per_city(df1):
    df_aux = (df1.loc[:, ['restaurant_id', 'city', 'country_name']]
                 .groupby(['city', 'country_name'])
                 .count()
                 .sort_values('restaurant_id', ascending=False)
                 .reset_index()
                 .head(10))
    fig = px.bar(df_aux, x='city', y='restaurant_id', color='country_name', text_auto=True, labels={"city": "Cidade", "restaurant_id": "Quantidade de Restaurantes", "country_name": "Países"})
    fig.update_traces(textfont_size=13, textangle=0, textposition='outside', cliponaxis=False)
    return fig

# Função para plotar gráfico das 7 cidades com avaliação acima de 4
def rating_over_4(df1):
    df_aux = (df1.loc[(df1['aggregate_rating'] >= 4), ['restaurant_id', 'aggregate_rating', 'city', 'country_name']]
                 .groupby(['city', 'country_name'])
                 .count()
                 .sort_values('aggregate_rating', ascending=False)
                 .reset_index()
                 .head(7))
    fig = px.bar(df_aux, x='city', y='restaurant_id', color='country_name', text_auto=True, labels={"city": "Cidade", "restaurant_id": "Quantidade de Restaurantes", "country_name": "Países"})
    fig.update_traces(textfont_size=13, textangle=0, textposition='outside', cliponaxis=False)
    return fig

# Função para plotar gráfico das 7 cidades com avaliação abaixo de 2.5
def rating_under_25(df1):
    df_aux = (df1.loc[(df1['aggregate_rating'] <= 2.5), ['restaurant_id', 'aggregate_rating', 'city', 'country_name']]
                 .groupby(['city', 'country_name'])
                 .count()
                 .sort_values('aggregate_rating', ascending=False)
                 .reset_index()
                 .head(7))
    fig = px.bar(df_aux, x='city', y='restaurant_id', color='country_name', text_auto=True, labels={"city": "Cidade", "restaurant_id": "Quantidade de Restaurantes", "country_name": "Países"})
    fig.update_traces(textfont_size=13, textangle=0, textposition='outside', cliponaxis=False)
    return fig

# Função para plotar o gráfico com as 10 cidades com mais tipos de culinária distintos
def cities_dist_cuisines(df1):
    df_aux = (df1.loc[:, ['cuisines', 'city', 'country_name']]
                 .groupby(['city', 'country_name'])
                 .nunique()
                 .sort_values('cuisines', ascending=False)
                 .reset_index()
                 .head(10))
    fig = px.bar(df_aux, x='city', y='cuisines', color='country_name', text_auto=True, labels={"city": "Cidade", "cuisines": "Quantidade de Culinárias", "country_name": "Países"})
    fig.update_traces(textfont_size=13, textangle=0, textposition='outside', cliponaxis=False)
    return fig

#==================================================================
# Barra Lateral Streamlit
#==================================================================
st.set_page_config(page_title='Main', layout='wide')

st.sidebar.header('Filtros')

# Filtro seleção de países
all_countries = df1['country_name'].unique()
countries = st.sidebar.multiselect('Escolha os países que deseja visualizar:', 
                                   df1['country_name'].unique(),
                                  default=all_countries)
linhas_selecionadas = df1['country_name'].isin(countries)
df1 = df1.loc[linhas_selecionadas, :]

st.sidebar.markdown("""___""")

# Copy
image = Image.open('logo-white-transparent.png')
st.sidebar.image(image, width=190)
st.sidebar.markdown('### by Alexandre Faizibaioff')
st.sidebar.markdown("""___""")

#==================================================================
# Layout da página
#==================================================================
st.header('Fome Zero - Cities Page')
st.subheader('Confira informações sobre as cidades presentes na plataforma')
st.markdown("""___""")

with st.container():
    st.markdown('##### Top 10 - Cidades com mais restaurantes')
    fig = count_rest_per_city(df1)
    st.plotly_chart(fig, use_container_width=True)
    
st.markdown("""___""")
with st.container():
    
    col1, col2  = st.columns(2)
    
    with col1:
        st.markdown('##### Cidades c/ mais restaurantes: nota acima de 4')
        fig = rating_over_4(df1)
        st.plotly_chart(fig, use_container_width=True)
      
    with col2:
        st.markdown('##### Cidades c/ mais restaurantes: nota abaixo de 2.5')
        fig = rating_under_25(df1)
        st.plotly_chart(fig, use_container_width=True)
    
st.markdown("""___""")
with st.container():
    st.markdown('##### Top 10 - Cidades com mais tipos de culinária distintos')
    fig = cities_dist_cuisines(df1)
    st.plotly_chart(fig, use_container_width=True)
