fetch ("http://127.0.0.1:8000/municipios")
.then(res => res.json())
.then(data =>{
    const selector = document.getElementById("selector-municipio");
    data.municipios.forEach(municipio => {
        const option =document.createElement("option");
        option.value =municipio
        option.textContent =municipio
        selector.appendChild(option);
    })
    selector.addEventListener("change",function(){
        
        fetch("http://127.0.0.1:8000/produccion/" + selector.value)
        .then(res => res.json())
        .then(data =>{
            const tabla=document.createElement("table");
            const encabezado = document.createElement("tr");
            const th1 = document.createElement("th");
            th1.textContent = "Cultivo";
            const th2 = document.createElement("th");
            th2.textContent="Año"
            const th3 = document.createElement("th");
            th3.textContent="Producción"
            encabezado.appendChild(th1);
            encabezado.appendChild(th2);
            encabezado.appendChild(th3);
            tabla.appendChild(encabezado);
             data.forEach(registro => {
                const fila = document.createElement("tr")
                const td1 = document.createElement("td")
                td1.textContent = registro.Cultivo
                const td2 = document.createElement("td")
                td2.textContent = registro.Año
                const td3 = document.createElement("td")
                td3.textContent = registro.Producción
                fila.appendChild(td1)
                fila.appendChild(td2)
                fila.appendChild(td3)
                tabla.appendChild(fila)
            })

            document.getElementById("resultados").innerHTML = ""
            document.getElementById("resultados").appendChild(tabla)
            const cultivos=[...new Set(data.map(r => r.Cultivo))]
            const años=[...new Set(data.map(r => r.Año))]
            const dataset = cultivos.map(cultivo => {
                return {
                    label: cultivo,
                    data: años.map(año => {
                        const registro = data.find(r => r.Cultivo === cultivo && r.Año === año);
                        return registro ? registro.Producción : 0;
                    })
                }
            })
            const ctx =document.getElementById("grafica")
            if(window.graficaActual) window.graficaActual.destroy();
            window.graficaActual = new Chart(ctx, {
                type: "line",
                data: {labels: años, datasets: dataset}
        })
    })
    
 



})
})