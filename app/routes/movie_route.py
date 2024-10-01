from typing import Any
from fastapi import APIRouter, Depends, Query
from bson import json_util
import json
from app.Enums.gender import Gender
from app.Enums.occupation import Occupation
from app.services.movie_service import MovieService

movie_route = APIRouter(
    prefix="/movie",
    tags=["movie"]
)

@movie_route.get("/")
def get_movies(genre: Gender = Query(..., description="Gender of the user (Male or Female)"),
               age: int = Query(..., description="Age of the user"),
               occupation: Occupation = Query(..., description="Occupation of the user")):
    
    movie_service = MovieService()
    
    gender_index = 0 if genre == Gender.male else 1
    occupation_index = list(Occupation).index(occupation)
    
    recommended_movies = movie_service.get_recommended_movies(gender_index, age, occupation_index)
    
    return json_util.dumps(recommended_movies)
