from fastapi import FastAPI
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
    