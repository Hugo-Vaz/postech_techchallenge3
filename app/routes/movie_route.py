from typing import Any
from fastapi import APIRouter, Depends, Query
from bson import json_util
import json
from app.Enums.gender import Gender
from app.services.movie_service import MovieService

movie_route = APIRouter(
    prefix="/movie",
    tags=["movie"]
)


@movie_route.get("/")
def get_movies(genre: Gender = Query(..., description="Gender of the user (M or F)"),
               age: int = Query(..., description="Age of the user"),
               nationality: str = Query(..., description="Nationality")):
    
    movie_service = MovieService()
    
    recommended_movies = movie_service.get_recommended_movies(genre, age, nationality)
    
    return json_util.dumps(recommended_movies)