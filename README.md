# 1- Problema de Negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO  também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita  uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez. O CEO precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.

## Geral

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## País

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Cidade

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

## Restaurantes

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

## Tipos de Culinária

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

# 2- Premissas do negócio

1. A análise foi realizada com dados gerados no dia 10/04/2019
2. Marketplace foi o modelo de negócio assumido.
3. As 3 principais formas de agrupar os dados foram por países, por cidades e por tipos culinários

# 3- Estratégia da solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem os principais dados dos agrupamentos utilizado.

1. Agrupamento Geral
2. Agrupamento por País
3. Agrupamento por Cidades
4. Agrupamento por Tipos de Culinárias

Cada Agrupamento é representado pelo seguinte conjunto de métricas.

## 1. Agrupamento Geral
    a. Quantos restaurantes únicos estão registrados?
    b. Quantos países únicos estão registrados?
    c. Quantas cidades únicas estão registradas?
    d. Qual o total de avaliações feitas?
    e. Qual o total de tipos de culinária registrados?
    
## 2. Agrupamento por País
    a. Qual o nome do país que possui mais cidades registradas?
    b. Qual o nome do país que possui mais restaurantes registrados?
    c. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
    d. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
    e. Qual o nome do país que possui a maior quantidade de avaliações feitas?
    f. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
    g. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
    h. Qual o nome do país que possui, na média, a maior quantidade de avaliações registradas?
    i. Qual o nome do país que possui, na média, a maior nota média registrada?
    j. Qual o nome do país que possui, na média, a menor nota média registrada?
    k. Qual a média de preço de um prato para dois por país?
    
## 3. Agrupamento por Cidades
    a. Qual o nome da cidade que possui mais restaurantes registrados?
    b. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
    c. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
    d. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
    e. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
    f. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
    g. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
    h. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
    
## 4. Agrupamento por Restaurantes
    a. Qual o nome do restaurante que possui a maior quantidade de avaliações?
    b. Qual o nome do restaurante com a maior nota média?
    c. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
    d. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
    e. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
    f. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
    g. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
    h. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
    
## 5. Agrupamento por Tipos de Culinária
    a. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
    b. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
    c. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
    d. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
    e. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
    f. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
    g. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
    h. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
    i. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
    j. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
    k. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
    l. Qual o tipo de culinária que possui a maior nota média?
    m. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

# 4- Top 3 Insights de dados

1. A India possui 5 das cidades com maior numero de restaurantes registrados.
2. Comida do tipo ‘Afegã’ é o tipo de culinária com a nota mais baixa na média de avaliação.
3. ‘Ramen’ é considerado o melhor tipo de culinária, considerando a média de avaliação e desconsiderando ‘Others’ como tipo de culinária.

# 5- O produto final do projeto

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através desse link: (url do streamlit cloud)

# 6- Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

# 7- Próximo passos
