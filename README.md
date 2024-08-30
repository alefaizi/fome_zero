# Fome Zero
## 1. Problema de Negócio

A empresa Fome Zero é uma marketplace de restaurantes. Seu core business é facilitar o encontro e negociações entre clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a plataforma. Para isso, ele precisa que seja feita uma análise nos dados da empresa para responder as seguintes perguntas:

Perguntas Gerais

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

Perguntas sobre países:

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária
distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

Perguntas sobre cidades:

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

Perguntas sobre restaurantes:

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

Perguntas sobre tipos de culinária:

1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O CEO também pediu que fosse gerado um dashboard que permita visualizar as principais informações e insights referentes as perguntas auxiliando na tomada de decisões mais assertivas.

## 2. Premissas assumidas para análise

- O modelo de negócio assumido, de acordo com o problema proposto foi o de Marketplace;
- Foram retirados 585 registros em duplicidade e 13 linhas que continham dados nulos na base original. O dataset limpo contém 6.929 registros;
- Para uma melhor compreensão dos dados referentes ao 'valor médio para duas pessoas', todos os preços foram convertidos para dólares americanos (USD) com base nas cotações do dia 24/08/2024;
- Foi identificado 1 outlier na coluna de 'valor médio para duas pessoas' que foi substituído;
- Restaurantes com mais de um tipo de culinária, tiveram o primeiro registro considerado como principal e os demais foram descartados.

## 3. Estratégia da solução

O painel estratégico foi desenvolvido utilizando as principais visões e insights obtidos após responder mais de 45 perguntas de negócio:

Home Page:

1. Resumo do projeto, principais premissas, ferramentas e linguagens utilizadas.

Main Page:

1. Cards com os principais números: restaurantes cadastrados, países, cidades, número de avaliações e tipos de culinária;
2. Mapa interativo com a localização dos restaurantes e informações de nome, cidade e avaliação (utilizei um marcador que muda de cor de acordo com a nota do estabelecimento).

Countries Page:

1. Quantidade de restaurantes por país;
2. Quantidade de cidades por país;
3. Média de avaliações por país;
4. Média de preço de um prato para duas pessoas por país em dólares americanos (USD).

Cities Page:

1. Top 10 cidades com mais restaurantes;
2. Cidades com mais restaurantes que possuem nota acima de 4;
3. Cidades com mais restaurantes que possuem nota abaixo de 2,5;
4. Top 10 cidades com mais tipos de culinária distintos.

Cuisines Page:

1. Cards com os restaurantes mais bem avaliados de culinária italiana, americana, árabe, japonesa e outras;
2. Tabela com informações dos top 10 restaurantes mais bem avaliados;
3. Top 10 melhores tipos de culinária;
4. Top 10 piores tipos de culinária.

## 4. Top 3 Insights de dados

1. O preço de um prato para duas pessoas varia consideravelmente entre os países. A África do Sul (mais caro) tem um custo médio 50x maior que a Turquia (mais barato);
2. Restaurantes que fazem pedidos online possuem 2x mais avaliações registradas do que restaurantes que não aceitam pedidos online. A média das avaliações difere em 0.04. Podemos assumir que aceitar pedidos online é vantajoso para o restaurante, pois gera o dobro de avaliações (e consequentemente mais vendas) com baixo impacto na nota;
3. Restaurantes que fazem reservas tem um valor médio para dois US$ 0,06 menor do que os que não aceitam reservas, portanto podemos assumir que esse critério não influencia no preço.

## 5. O produto final do projeto

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link: https://acsf-fomezero.streamlit.app/

## 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos, tabelas e visualizações que exibam as métricas da melhor forma possível para o CEO. Através da análise dos dados com Python foi possível responder a todas as perguntas feitas e algumas outras que surgiram durante o processo. Para o dashboard foram selecionadas as informações mais relevantes observadas ao longo do processo. Foi criado um filtro na barra lateral para seleção de países específicos individualmente ou combinados; ao fazer a seleção, todo Dashboard é ajustado de acordo com os critérios escolhidos.

## 7. Próximos passos

- Incluir mais filtros;
- Criar mais visões de negócio;
- Melhorar os scripts Python;
- Responder novas perguntas explorando mais afundo o dataset.
