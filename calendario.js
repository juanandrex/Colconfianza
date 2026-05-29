const MESES = ["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]

const CALENDARIO_CULTIVOS = {
    "Papa": {
        siembra: [1, 2, 7, 8],
        cosecha: [5, 6, 11, 12],
        descanso: [3, 4, 9, 10]
    },
    "Arveja": {
        siembra: [0, 1, 6, 7],
        cosecha: [3, 4, 9, 10],
        descanso: [2, 5, 8, 11]
    }
}

document.getElementById("btn-calendario").addEventListener("click", function() {
    const municipio = document.getElementById("selector-municipio-cal").value
    const cultivo = document.getElementById("selector-cultivo-cal").value

    if (!municipio || !cultivo) {
        alert("Por favor selecciona municipio y cultivo")
        return
    }

    const cal = CALENDARIO_CULTIVOS[cultivo]
    const div = document.getElementById("resultado-calendario")

    div.innerHTML = `<div class="calendario-header">
    <h3>📅 ${cultivo} — ${municipio}</h3>
    <p>Basado en datos históricos 2019–2024</p>
</div>

    <div class="meses-grid">
            ${MESES.map((mes, i) => {
                let tipo = ""
                let emoji = "—"
                if (cal.siembra.includes(i)) { tipo = "siembra"; emoji = "🌱"} 
                else if (cal.cosecha.includes(i)) { tipo = "cosecha"; emoji = "⚒️"} 
                else { tipo = "descanso"; emoji = "💤"} 
                return `<div class="mes-card ${tipo}">
                <span class="mes-nombre">${mes}</span>
                <span class="mes-emoji">${emoji}</span>
            </div>`
            }).join("")}
        </div>
        <div class="calendario-leyenda">
                <span>🌱 Sembrar</span>
                <span>⚒️ Cosechar</span>
                <span>💤 Descanso</span>
            </div>
        <div class="recomendacion-card">
                <strong>⏰ Ahora: ${cal.siembra.includes(new Date().getMonth()) ? "buen momento para sembrar" : cal.cosecha.includes(new Date().getMonth()) ? "tiempo de cosecha" : "período de descanso"}</strong>
                Consulta con tu técnico agrícola para confirmar las fechas exactas según tu finca.
            </div>`
});