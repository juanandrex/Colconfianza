const MUNICIPIOS_COORDS = {
    "Chocontá":    { lat: 5.0833, lon: -73.6833 },
    "Machetá":     { lat: 5.0833, lon: -73.5500 },
    "Manta":       { lat: 4.9833, lon: -73.6167 },
    "Sesquilé":    { lat: 5.0500, lon: -73.7833 },
    "Suesca":      { lat: 5.1000, lon: -73.8000 },
    "Tibirita":    { lat: 5.0333, lon: -73.5000 },
    "Villapinzón": { lat: 5.2167, lon: -73.5833 }
}

document.getElementById("btn-analizar").addEventListener("click", function() {
    const municipio = document.getElementById("selector-municipio-plaga").value
    const cultivo = document.getElementById("selector-cultivo-plaga").value

    if (!municipio || !cultivo) {
        alert("Por favor selecciona municipio y cultivo")
        return
    }

    const coords = MUNICIPIOS_COORDS[municipio]

    fetch(`https://api.open-meteo.com/v1/forecast?latitude=${coords.lat}&longitude=${coords.lon}&current=temperature_2m,relative_humidity_2m&timezone=auto`)
    .then(res => res.json())
    .then(clima => {
        const temperatura = clima.current.temperature_2m
        const humedad = clima.current.relative_humidity_2m

        Promise.all([
            fetch(`http://127.0.0.1:8000/riesgos/${cultivo}?temperatura=${temperatura}&humedad=${humedad}`).then(r => r.json()),
            fetch(`http://127.0.0.1:8000/plagas/${cultivo}`).then(r => r.json())
        ]).then(([riesgos, plagas]) => {
            const div = document.getElementById("resultado-plagas")
            div.innerHTML = `<p>s${municipio}: ${temperatura}°C · ${humedad}% humedad</p>`

            if (riesgos.riesgos.length === 0) {
                div.innerHTML += "<p> Sin riesgo detectado</p>"
            } else {
                div.innerHTML += `<h3> Riesgos detectados:</h3>`
                riesgos.riesgos.forEach(nombrePlaga => {
                    const plaga = plagas.find(p => p.nombre === nombrePlaga)
                    div.innerHTML += `<div class="plaga-card">
                        <h4> ${nombrePlaga}</h4>
                        <p>${plaga ? plaga.descripcion : ""}</p>
                        <h5>Productos recomendados:</h5>
                        ${plaga ? plaga.productos.map(p => `
                            <p><strong>${p.nombre}</strong> — ${p.dosis} — ${p.tipo}</p>
                        `).join("") : ""}
                    </div>`
                })
            }
        })
    })
})