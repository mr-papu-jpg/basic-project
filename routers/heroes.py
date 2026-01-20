from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import Optional

router= APIRouter(
    prefix="/heroes",
    tags=["Heroes"]
)

class Heroe(BaseModel):
    id: int
    nombre: str
    super_poder: str
    nivel_fuerza: int
    esta_activo: Optional[bool] = True

base_de_datos_heroes = []

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_heroe(heroe: Heroe):
    if heroe.nivel_fuerza > 100:
        raise HTTPException(status_code=400, detail="La fuerza debe ser menor de 100")

    base_de_datos_heroes.append(heroe.dict())
    return {"mensaje": "Héroe guardado", "datos": heroe}

@router.get("/")
def listar_heroes(poder: Optional[str] = None):
    if poder:
        resultados = [u for u in base_de_datos_heroes if u["super_poder"].lower() == poder.lower()]
        return resultados
    return base_de_datos_heroes

@router.get("/{heroe_id}")
def obtener_heroe(heroe_id: int):
    for h in base_de_datos_heroes:
        if h["id"] == heroe_id:
            return h
    raise HTTPException(status_code=404, detail="Héroe no encontrado")

@router.delete("/{heroe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_heroe(heroe_id: int):
    for index, h in enumerate(base_de_datos_heroes):
        if h["id"] == heroe_id:
            base_de_datos_heroes.pop(index)
            return None

    raise HTTPException(status_code=404, detail="ID no encontrado")
