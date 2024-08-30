#==================================================================
# Libraries
#==================================================================
import streamlit as st
from PIL import Image

#==================================================================
# Barra Lateral Streamlit
#==================================================================
st.set_page_config(page_title="Home", layout='wide')

image = Image.open('logo-white-transparent.png')
st.sidebar.image(image, width=190)
st.sidebar.markdown('### by Alexandre Faizibaioff')
st.sidebar.markdown("""___""")

#st.sidebar.header('Dados tratados')
#st.sidebar.download_button('Download', data='\v3_fome_zero.ipynb')

#==================================================================
# Layout da página
#==================================================================
st.title("Fome Zero")
st.markdown("""___""")
st.markdown(
    """
    Projeto desenvolvido na disciplina 'Analisando Dados com Python' da Comunidade DS.
    
    #### Sobre o projeto
    - **Resumo**:
        - Todo o projeto foi desenvolvido a partir da base de dados de um marketplace de restaurantes. No dataset existem diversas informações como localização, tipo de culinária, avaliação dos clientes, preço médio, possibilidade de reservas, entrega a domicílio, entre outras.
        - O trabalho foi divido em duas partes:
            1) Na primeira parte foi feita uma limpeza e análise dos dados onde respondi mais de 45 perguntas de negócio utlizando Python e suas bibliotecas;
            2) Na segunda parte foi feito um Dashboard no Streamlit com as principais informações, insights e filtros interativos para que outros usuários possam explorar os dados e extrair insights.
    - **Premissas**:
        - Foram retirados 585 registros em duplicidade e  13 linhas que continham dados nulos na base original. O dataset limpo contém 6.929 registros;
        - Para uma melhor compreensão dos dados referentes ao 'valor médio para duas pessoas', todos os preços foram convertidos para dólares americanos (USD) com base nas cotações do dia 24/08/2024.
    - **Ferramentas e linguagens utilizadas**:
        - JupyterLab;
        - Python;
        - Streamlit.
        
    #### Contato
    - Fique à vontade para entrar em contato, obter mais informações e enviar sugestões:
        - E-mail: ale.faizi@gmail.com
        - LinkedIn: https://www.linkedin.com/in/alexandrecsf/
        - Para mais informações acesse o README
""")
st.markdown("""___""")
