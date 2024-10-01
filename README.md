# Projeto de Identificação e sugestão de filmes

## Problema a ser Resolvido

O objetivo deste projeto é identificar a correlação entre os dados dos usuários (idade, gênero e ocupação) e suas preferências por filmes, com base nas avaliações feitas por outros usuarios parecidos. A partir desse modelo, criaremos uma API que, com base em alguns dados de um usuário, seja capaz de sugerir filmes que talvez sejam do seu interesse, como o as recomendações da Netflix, por exemplo.

### Grupo de Dados Utilizado:
Usaremos o dataset **MovieLens 1M**:
- [movie_lens-1m](https://files.grouplens.org/datasets/movielens/ml-1m.zip)

## Etapas do Projeto:

1. **Correlacionar os 3 datasets (usuários, ratings e filmes)**:
   - O primeiro passo será integrar os dados dos usuários, suas avaliações e os dados dos filmes.

2. **Classificação das Notas dos Filmes**:
   - As avaliações dos usuários serão agrupadas para simplificar a análise:
     - **0 a 2**: Detestei = 1
     - **3 a 5**: Não Gostei = 2
     - **6 a 8**: Gostei = 3
     - **9 a 10**: Adorei = 4

3. **Escolha de um Modelo Supervisionado**:
   - Será selecionado um modelo de machine learning supervisionado.
   - O modelo escolhido será aquele que apresentar o melhor desempenho, e menor taxa de erro nas previsões.

4. **Testes e Resultados**:
   - Todos os testes realizados serão salvos e documentados, pois fazem parte do processo de avaliação.

5. **Criação da API**:
   - Após a definição e treinamento do modelo, uma API será construída com o principal objetivo de:
     - **Sugerir filmes para um usuário fictício**: Com base em informações como gênero, idade e ocupação, sugerir top 5 filmes adequados.

6. **Documentação do Processo**:
   - Todo o processo de exploração de dados, testes e escolha do modelo será documentado e codificado em um notebook, facilitando a execução e visualização por parte do avaliador.

7. **Armazenamento do Modelo**:
   - Após o treinamento, o modelo será salvo no formato .sav na S3, fazendo uso do modulo [pickle](https://docs.python.org/3/library/pickle.html#module-pickle) do Python.

