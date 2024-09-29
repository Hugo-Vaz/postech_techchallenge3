from fastapi import FastAPI, Depends
from app.routes.movie_route import movie_route

app = FastAPI(
    title="Movie Gender Correlation"
)

app.include_router(movie_route)
