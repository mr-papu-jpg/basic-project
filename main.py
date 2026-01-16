from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return {"status": "Servidor corriendo"}

@app.get("/multiplicar/{numero}")
def multiplicar(numero: int):
    return {"resultado": numero * 2}
