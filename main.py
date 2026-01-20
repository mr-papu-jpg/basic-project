from fastapi import FastAPI
from routers import heroes

app = FastAPI()

app.include_router(heroes.router)

@app.get("/")
def home():
    return {"Mensaje": "Bienvenido a la API central"}
