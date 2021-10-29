let parameters = []
function removeElement(event, position) {
    swal({
        title: "¿Quieres borrar este par ordenado?",
        text: "Las coordenadas serán eliminadas " + position,
        type: "warning",//Logo de cuidado :v
        showCancelButton: true,
        confirmButtonColor: "#DD6B5F",
        confirmButtonText: "Si, quiero eliminarlas",
        cancelButtonText: "Cancelar",
        closeOnConfirm: false
    },
        function () {
            swal("Coordenadas eliminadas", "Par ordenado eliminado del arreglo", "success");
            event.target.parentElement.remove()
            delete parameters[position]
        });
}

const addJsonElement = json => {
    parameters.push(json)
    return parameters.length - 1
}

(function load() {
    const form = document.getElementById("formCoordenadas");
    const divElements = document.getElementById("divElements");
    const btnCalculate = document.getElementById("btnCalculate");
    const btnAdd = document.getElementById("btnAdd");
    const templateElement = (xvalue, yvalue, position) => {
        return (`
            <div class="card-panel blue darken-2">
            <span class="white-text" style="font-size: 32px;">p${position}(x,y) = [ ${xvalue} , ${yvalue} ]
            </span><br>
            <button type="button" class="waves-effect waves-light btn-large light-blue darken-4" onclick="removeElement(event, ${position})">
            <i class="zmdi zmdi-minus-circle left"></i>Eliminar</button>
            </div>
        `)
    }

    btnAdd.addEventListener("click", (evento) => {
        if (form.coorX.value != "" && form.coorY.value != "") {
            let index = addJsonElement({
                x: form.coorX.value,
                y: form.coorY.value
            });
            const div = document.createElement("div");
            div.classList.add("col", "l12");
            div.innerHTML = templateElement(form.coorX.value, form.coorY.value, index);
            divElements.insertBefore(div, divElements.firstChild);
            form.reset();
        } else {
            swal("Datos incorrectos", "Ingresa las coordenadas adecuadamente", "error");
        }
    });

    btnCalculate.addEventListener("click", (evento) => {
        parameters = parameters.filter(element => element != null);
        if (parameters.length > 2) {
            const jsonDiv = document.getElementById("jsonArea");
            dataJson = JSON.stringify(parameters);
            jsonDiv.innerHTML = dataJson;
            swal({
                title: "¿Desea realizar los calculos?",
                text: "Esto tomará unos segundos",
                type: "info",
                showCancelButton: true,
                closeOnConfirm: false,
                showLoaderOnConfirm: true
            },
                function () {
                    $.ajax({
                        type: "POST",
                        url: "/calculate",
                        data: {
                            arreglo: dataJson
                        },
                        cache: false,
                        success: function (response) {
                            swal("Cálculo exitoso");
                            divElements.innerHTML = "";
                            parameters = [];
                            jsonDiv.innerHTML = "";
                            let ingresaDatos = document.getElementById("ingresaDatos");
                            ingresaDatos.style.display = "none";
                            let muestraDatos = document.getElementById("muestraDatos");
                            muestraDatos.style.display = "block";
                            let areaDatos = document.getElementById("areaDatos");
                            areaDatos.value = response;
                            let grafica = document.getElementById("grafica");
                            grafica.setAttribute("src", "/static/img/grafica.png");
                        },
                        error: function (response) { swal("Server Error", response); }
                    })
                }
            );

        } else {
            swal("Faltan Datos", "Se necesitan más coordenada", "error");
        }
    });

})()