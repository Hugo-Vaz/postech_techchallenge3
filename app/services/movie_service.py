import boto3
import os
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class MovieService:
    def get_movies_from_s3(self):
        bucket_name = 'techchallengegp53'
        s3_file_key = 'movie_data.dat'
        local_file_path = 'movie_data.dat'

        try:
            s3 = boto3.client(
                's3',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                aws_session_token=os.getenv('AWS_SESSION_TOKEN')
            )
            s3.download_file(bucket_name, s3_file_key, local_file_path)
            print(f"Arquivo baixado com sucesso do S3: {local_file_path}")
        except (NoCredentialsError, ClientError) as e:
            print(f"Erro ao conectar ao bucket S3: {e}")
            fake_local_file_path = os.path.join('fakeBucket', s3_file_key)
            if os.path.exists(fake_local_file_path):
                local_file_path = fake_local_file_path
                print(f"Carregando arquivo do fakeBucket: {fake_local_file_path}")
            else:
                print("Arquivo não encontrado no S3 e nem localmente.")
                return None

        try:
            with open(local_file_path, 'r', encoding='ISO-8859-1') as file:
                data = file.readlines()
                return data
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return None

    def get_recommended_movies(self, genre, age, nationality):
        movie_data = self.get_movies_from_s3()

        if not movie_data:
            return {"error": "Sem Dados"}

        current_year = datetime.now().year
        birth_year = current_year - age

        recommended_movies = []
        for line in movie_data:
            fields = line.split("::")
            if len(fields) > 2:
                try:
                    movie_year = int(fields[2])
                    if movie_year == birth_year:
                        recommended_movies.append(fields[1])  # 1 é o titulo do filme
                except ValueError:
                    print(f"Falha o converter ano para int. Pulando registro")
                    continue 

        if recommended_movies:
            return {"recommended_movies": recommended_movies}
        else:
            return {"message": "Nenhum filme encontrado para o ano de nascimento correspondente."}
