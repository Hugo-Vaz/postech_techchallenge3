import boto3
import os
import pandas as pd
import pickle
from sklearn.preprocessing import MultiLabelBinarizer, LabelEncoder
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
    
class MovieService:

    # Conectando ao S3 (tem que pegar no labs a key e colocar no .nev. 
    # Lembre-se de mudar o prefixo padrão AWS para S3)
    def get_s3_client(self):
        """Retorna um cliente S3 configurado com as credenciais."""
        try:
            s3 = boto3.client(
                's3',
                aws_access_key_id=os.getenv('S3_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('S3_SECRET_ACCESS_KEY'),
                aws_session_token=os.getenv('S3_SESSION_TOKEN')
            )
            return s3
        except NoCredentialsError:
            print("Credenciais AWS não encontradas.")
            return None

    def get_movies_from_s3(self):
        bucket_name = 'techchallengegp53'
        s3_file_key = 'raw/movies.dat'
        local_file_path = './raw/ml-1m/movies.dat' 

        try:
            s3 = self.get_s3_client()
        
            # Baixando o arquivo do S3
            s3.download_file(bucket_name, s3_file_key, local_file_path)
            print(f"Arquivo baixado do S3: {local_file_path}")
        except (NoCredentialsError, ClientError) as e:
            print(f"Erro ao conectar ao bucket: {e}")
            if os.path.exists(local_file_path):
                # Verificando se o arquivo existe no local
                print(f"Carregando arquivo local: {local_file_path}")
            else:
                print("Arquivo não encontrado no S3 e nem localmente :(.")
                return None

        return local_file_path

    def prepare_data(self, local_file_path, genre, age, occupation):
        
        # Carregar dados do arquivo movie_data.da
        movies_data = pd.read_csv(local_file_path, sep='::', header=None, names=['movieid', 'title', 'genres'], encoding='iso-8859-2', engine='python')
        
        # Separar gêneros por |
        movies_data['genres'] = movies_data["genres"].str.split("|")
        
        # Transformar gêneros em colunas binárias
        mlb = MultiLabelBinarizer()
        encoded_data = mlb.fit_transform(movies_data['genres'])
        dados_encodados = pd.DataFrame(encoded_data, columns=mlb.classes_)
        
        # Concatenar com dados dos filmes
        dados_encodados = pd.concat([dados_encodados, movies_data], axis=1)
        dados_encodados = dados_encodados.drop(['genres'], axis=1)
        
        print(genre)
        print(age)
        print(occupation)
        
        # Adicionar colunas nos inputs
        dados_encodados['gender'] = genre
        dados_encodados['age'] = age
        dados_encodados['occupation'] = occupation
        
        # Transforma os generos em valores numéricos
        label_encoder = LabelEncoder()
        dados_encodados['gender'] = label_encoder.fit_transform(dados_encodados['gender'])
        
        return dados_encodados

    def load_model(self):
        bucket_name = 'techchallengegp53'
        s3_file_key = 'modelo/XGBoost.sav'  # Caminho no bucket S3
        local_file_path = './playground/modelo-xgboost.sav'  # Caminho local

        try:
            # tentar baixar o modelo
            s3 = self.get_s3_client()
            s3.download_file(bucket_name, s3_file_key, local_file_path)
            print(f"Modelo baixado do S3: {local_file_path}")
        except (NoCredentialsError, ClientError) as e:
            print(f"Erro ao conectar ao bucket: {e}")
            
            if os.path.exists(local_file_path):
                # Se falhar, tentar carregar o modelo localmente
                print(f"Carregando modelo local: {local_file_path}")
            else:
                print("Modelo não encontrado no S3 e nem localmente.")
                return None

        # Carregar o modelo XGBoost do caminho local (seja ele baixado ou já existente)
        try:
            with open(local_file_path, 'rb') as f:
                modelo = pickle.load(f)
            return modelo
        except FileNotFoundError:
            print("Modelo XGBoost não encontrado no caminho loca.")
            return None

    def predict_ratings(self, modelo, dados_encodados):
        ratings = []

        for index, row in dados_encodados.iterrows():
            # Remove as colunas desnecessárias para a predição
            dataset = row.drop(['title', 'movieid'])
            
            # Realza a predição com o modelo
            pred = modelo.predict([dataset])
            
            # Salva o título do filme e sua pontuação prevista
            ratings.append((row['title'], pred[0]))

        return ratings

    def get_top_recommendations(self, ratings, top_n=5):
        """Ordena e retorna os principais filmes recomendados."""
        # Ordenar as classificações
        ratings.sort(key=lambda e: e[1], reverse=True)
        
        # Retornar os top N filmes recomendados
        return ratings[:top_n]

    def get_recommended_movies(self, genre, age, occupation):
        
        # Obter Arquivos
        file_path = self.get_movies_from_s3()

        if not file_path:
            return {"error": "Arquivo de filmes não encontrado."}
        
        # Preparar os dados dos filmes com os inputs do usuário
        data = self.prepare_data(file_path, genre, age, occupation)
        
        # Carregar o modelo treinado
        model = self.load_model()
        
        if model is None:
            return {"error": "Modelo não encontrado."}
        
        # Fazer a predição
        ratings = self.predict_ratings(model, data)
        
        # Obter os top 5 filmes recomendados
        top_5 = self.get_top_recommendations(ratings, top_n=5)
        
        # Retornar os filmes recomendados
        return {"recommended_movies": [movie[0] for movie in top_5]}