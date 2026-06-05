import pandas as pd
import numpy as np

df = pd.read_csv("Evaluaciones_Agropecuarias_Municipales__EVA._2019_-_2024._Base_Agrícola_20260520.csv")

for col in ["Área sembrada", "Área cosechada", "Producción", "Rendimiento"]:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(".", "", regex=False).str.replace(",", ".", regex=False), errors="coerce")

DOSIS_PRODUCTOS = {
    "Papa": {
        "Mancozeb 80%": 2,
        "Metalaxil + Mancozeb": 2.5,
        "Clorotalonil 72%": 1.5
    },
    "Arveja": {
        "Mancozeb 80%": 2,
        "Metalaxil": 2,
        "Spinosad": 0.5
    }
}


def predecir_demanda(municipio: str, cultivo: str):
    datos = df[(df["Municipio"] == municipio) & (df["Cultivo"] == cultivo)]
    
    if datos.empty:
        return None
    
    datos_agrupados = datos.groupby("Año")["Área sembrada"].sum().reset_index()
    
    x = datos_agrupados["Año"].values
    y = datos_agrupados["Área sembrada"].values
    
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    pendiente = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
    intercepto = y_mean - pendiente * x_mean
    
    area_lineal = pendiente * 2026 + intercepto
    if area_lineal <= 0:
         area_predicha = round(datos_agrupados["Área sembrada"].tail(3).mean(), 2)
    else:
        area_predicha = round(area_lineal, 2)
    
    productos = DOSIS_PRODUCTOS.get(cultivo, {})
    demanda = {}
    for producto, dosis in productos.items():
        litros_por_ha = dosis * 10
        demanda[producto] = round(area_predicha * litros_por_ha, 1)
    
    return {
        "municipio": municipio,
        "cultivo": cultivo,
        "area_predicha_2026": area_predicha,
        "demanda_estimada": demanda
    }