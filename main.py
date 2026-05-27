
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
import os
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


df= pd.read_csv ("Evaluaciones_Agropecuarias_Municipales__EVA._2019_-_2024._Base_Agrícola_20260520.csv")
for col in ["Área sembrada", "Área cosechada", "Producción", "Rendimiento"]:
    df[col] = pd.to_numeric (df [col].astype (str).str.replace (",", "."), errors="coerce")
@app.get("/")
def root ():
    return { "mensaje": "API ColConfianza activa"}
@app.get("/produccion")
def produccion ():
    resultado = df.groupby(["Municipio", "Cultivo", "Año"])["Producción"].sum().reset_index()
    return resultado.to_dict(orient="records")
@app.get ("/municipios")
def municipios ():
    resultado = df ["Municipio"].unique().tolist()
    return {"municipios": resultado}
@app.get("/produccion/{municipio}")
def produccion_nombre (municipio: str):
 resultado = df[df["Municipio"] ==municipio].groupby(["Cultivo", "Año"])["Producción"].sum().reset_index().round(2)
 return resultado.to_dict(orient="records")
@app.get("/cultivos/{nombre}")
def cultivos_nombre (nombre :str):
   resultado=df[df["Cultivo"]==nombre].groupby(["Municipio", "Año"])["Producción"].sum().reset_index()
   return resultado.to_dict(orient="records")
    

class Contacto(BaseModel):
    nombre: str
    correo: str
    telefono: str
    mensaje: str


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASS', ''),
        database=os.getenv('DB_NAME', 'colconfianza_db')
    )

@app.post('/contactos')
def crear_contacto(contacto: Contacto):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO contactos (nombre, correo, telefono, mensaje) VALUES (%s, %s, %s, %s)',
            (contacto.nombre, contacto.correo, contacto.telefono, contacto.mensaje)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {'status': 'ok', 'message': 'Contacto guardado correctamente'}
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail=f'Error al guardar contacto: {error}')
    
