from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

from starlette.types import HTTPExceptionHandler

app= FastAPI()


class Heroe(BaseModel):
    id: int
    nombre: str
    super_poder: str
    nivel_fuerza: int
    esta_activo: Optional[bool]= True


base_de_datos_heroes= []


@app.post("/heroes/")
def crear_juego(heroe: Heroe):
    if  heroe[nivel_fuerza] > 100:
        raise HTTPException(status_code=400, detail="La fuerza debe ser menor de 100")

    base_de_datos_heroes.append(heroe.dict())
    return {"mensaje":"heroe guardado", "datos": heroe}


@app.get("/heroes/")
def listar_heroes():
    return base_de_datos_heroes

@app.get("/poder/")
def listar_poder(poder: str= None):
    if poder: 
        resultados= [u for u in base_de_datos_heroes if u[poder].lower() == poder.lower()]
        return resultados
    return base_de_datos_heroes

@app.get("/poder/{id}")
def obtener_poder(heroe_id: int):
    for p in base_de_datos_heroes:
        if p[id] == heroe_id:
            return p 
        raise HTTPException(status_code=404, detail="Heroe no encontrado")


@app.delete("/heroes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_heroe(id: int):
    if id not in base_de_datos_heroes:
        raise HTTPException(status_code=404, detail="ID no encontrado")
    del base_de_datos_heroes[id]
    return {"mensaje":f"Heroe {id} fue eliminado."}
