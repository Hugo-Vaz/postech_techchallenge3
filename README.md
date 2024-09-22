# Projeto de Identificação de Preferências de Filmes e Sugerir Grupo Alvo

## Problema a ser Resolvido

O objetivo deste projeto é identificar a correlação entre os dados dos usuários (idade, gênero, nacionalidade, ocupação) e suas preferências por filmes, com base nas avaliações feitas. A partir desse modelo, criaremos uma API que, com base em alguns dados de um usuário, seja capaz de sugerir filmes adequados ou, com base nos dados de um filme, indicar o grupo alvo ideal para aquele filme.

### Grupo de Dados Utilizado:
Usaremos o dataset **MovieLens 1M**:
- [movie_lens1m-ratings](https://www.tensorflow.org/datasets/catalog/movie_lens?hl=pt-br#movie_lens1m-ratings)
- [movie_lens1m-movies](https://www.tensorflow.org/datasets/catalog/movie_lens?hl=pt-br#movie_lens1m-movies)

## Etapas do Projeto:

1. **Correlacionar os dois datasets (usuários e filmes)**:
   - O primeiro passo será integrar os dados dos usuários e suas avaliações com os dados dos filmes.

2. **Classificação das Notas dos Filmes**:
   - As avaliações dos usuários serão agrupadas para simplificar a análise:
     - **0 a 2**: Detestei = 1
     - **3 a 5**: Não Gostei = 2
     - **6 a 8**: Gostei = 3
     - **9 a 10**: Adorei = 4

3. **Escolha de um Modelo Supervisionado**:
   - Será selecionado um modelo de machine learning supervisionado.
   - O modelo escolhido será aquele que apresentar o melhor desempenho e acurácia nas previsões.

4. **Testes e Resultados**:
   - Todos os testes realizados serão salvos e documentados, pois fazem parte do processo de avaliação.

5. **Criação da API**:
   - Após a definição e treinamento do modelo, uma API será construída com dois métodos principais:
     - **Sugerir o grupo alvo para um novo filme**: Com base em seus dados, prever o público ideal.
     - **Sugerir filmes para um usuário fictício**: Com base em informações como gênero, idade e nacionalidade, sugerir N filmes adequados.

6. **Documentação do Processo**:
   - Todo o processo de exploração de dados, testes e escolha do modelo será documentado e codificado em um notebook, facilitando a execução e visualização por parte do avaliador.

7. **Armazenamento do Modelo (A SER DEFINIDO)**:
   - Após o treinamento, o modelo será salvo em um banco de dados **MongoDB** para facilitar sua reutilização e distribuição. 

8. **Gravação de Vídeo**:
   - Um vídeo será gravado detalhando todo o processo de construção do projeto, incluindo desde a coleta de dados até a implementação da API. Antes disso, um roteiro será preparado para guiar a gravação.

