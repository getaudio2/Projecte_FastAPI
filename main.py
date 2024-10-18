from fastapi import FastAPI,HTTPException

import db_alumnat
import alumnes

from typing import List

from pydantic import BaseModel

app = FastAPI()

class alumne(BaseModel):
    idAula: int
    nomAlumne: str
    cicle: str
    curs: int
    grup: str 

@app.get("/")
def read_root():
    return {"Alumnat API"}

@app.get("/alumne/list", response_model=List[dict])
def read_alumnes():
    return alumnes.alumnes_schema(db_alumnat.read())

@app.get("/alumne/show/{id}", response_model=alumne)
def read_alumnes_id(id:int):
    if db_alumnat.read_id(id) is not None:
        alumne = alumnes.alumne_schema(db_alumnat.read_id(id))
    else:
        raise HTTPException(status_code=404, detail="No s'ha trobat l'alumne")
    return alumne

@app.get("/alumne/listAll", response_model=List[dict])
def readAll():
  return alumnes.alumnesYAules_schema(db_alumnat.readAll())

@app.post("/alumne/add")
async def create_alumne(data: alumne):
    idAula = data.idAula
    nomAlumne = data.nomAlumne
    cicle = data.cicle
    curs = data.curs
    grup = data.grup
    l_alumne_id = db_alumnat.create(idAula,nomAlumne,cicle,curs,grup)
    return {
        "msg": "S'ha afegit correctament",
        "id alumne": l_alumne_id,
        "nom alumne": nomAlumne
    }

@app.put("/alumne/update/{id}")
def update_vots(id:int,cicle:str):
    updated_records = db_alumnat.update_alumne(id,cicle)
    if updated_records == 0:
       raise HTTPException(status_code=404, detail="No s'ha trobat l'alumne per actualitzar") 
    return {
        "msg": "S'ha modificat correctament",
        "id alumne": id
    }

@app.delete("/alumne/delete/{id}")
def delete_alumne(id:int):
    deleted_records = db_alumnat.delete_alumnat(id)
    if deleted_records == 0:
       raise HTTPException(status_code=404, detail="No s'ha trobat l'alumne a esborrar")
    return {
        "msg": "S'ha esborrat correctament",
        "id alumne": id
    }