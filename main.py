from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app= FastAPI()


class Heroe(BaseModel):
    nombre: str
    super_poder: str
    nivel_fuerza: int
    esta_activo: Optional[bool]= True


base_de_datos_heroes= []


@app.post("/heroes/")
def crear_juego(heroe: Heroe):
    base_de_datos_heroes.append(heroe.dict())
    return {"mensaje":"heroe guardado", "datos": heroe}


@app.get("/heroes/")
def listar_heroes():
    return base_de_datos_heroes
