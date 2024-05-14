from fastapi import FastAPI
from fastapi.responses import HTMLResponse 
# CREAR INSTANCIA DE FASTAPI
app = FastAPI()
app.title = "My first API"
app.version = "1.0.1"


#RUTA PARA LA API: PUNTO DE ENTRADA O ENDPOINT
@app.get("/", tags=["Start"]) #Nota: @:es un decorador (rutas) ; Tags; usado para cambio de etiqueta en documentación 

def message():
    return HTMLResponse ("<h1> Hello guys!, How are you?</h1>")


