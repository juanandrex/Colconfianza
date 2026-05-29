PLAGAS = {
    "Papa": [
        {
            "nombre": "Gota",
            "nombre_cientifico": "Phytophthora infestans",
            "condiciones": {
                "temp_min": 10,
                "temp_max": 18,
                "humedad_min": 80
            },
            "productos": [
                {"nombre": "Mancozeb 80%", "dosis": "2 g/litro", "tipo": "Económico"},
                {"nombre": "Metalaxil + Mancozeb", "dosis": "2.5 g/litro", "tipo": "Efectivo"},
                {"nombre": "Clorotalonil 72%", "dosis": "1.5 g/litro", "tipo": "Preventivo"}
            ],
            "descripcion": "Hongo que afecta hojas y tubérculos en condiciones frías y húmedas"
        },
        {
            "nombre": "Polilla guatemalteca",
            "nombre_cientifico": "Tecia solanivora",
            "condiciones": {
                "temp_min": 15,
                "temp_max": 25,
                "humedad_min": 60
            },
            "productos": [
                {"nombre": "Bacillus thuringiensis", "dosis": "1 kg/ha", "tipo": "Biológico"},
                {"nombre": "Clorpirifos", "dosis": "1.5 ml/litro", "tipo": "Químico"}
            ],
                    "descripcion": "Polilla que ataca tubérculos en campo y almacenamiento"

        }
    ],
    "Arveja": [
        {
            "nombre":"Mildeo velloso",
            "nombre_cientfico":"Peronospora viciae",
            "condiciones":{
                "temp_min": 8,
                "temp_max": 15,
                "humedad_min": 85
            },
            "productos":[
                {"nombre": "Mancozeb 80%", "dosis": "2 g/litro", "tipo": "Preventivo"},
                {"nombre": "Metalaxil", "dosis": "2 g/litro", "tipo": "Curativo"}
            ],
            "descripcion": "Hongo que causa manchas amarillas en hojas con condiciones frías"
    },
    {
        "nombre":"Trips",
        "nombre_cientifico": "Thrips tabaci",
        "condiciones":{
            "temp_min": 20,
            "temp_max": 30,
            "humedad_min": 40
        },
        "productos": [
                {"nombre": "Spinosad", "dosis": "0.5 ml/litro", "tipo": "Biológico"},
                {"nombre": "Imidacloprid", "dosis": "0.5 ml/litro", "tipo": "Sistémico"}
            ],
 "descripcion": "Insecto que daña flores y vainas en condiciones cálidas y secas"      
    }  
  ]
}



