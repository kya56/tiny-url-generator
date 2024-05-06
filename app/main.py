from fastapi import FastAPI
from app.routers import command, query


app = FastAPI()
app.include_router(command.router)
app.include_router(query.router)