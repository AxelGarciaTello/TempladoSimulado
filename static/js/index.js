let parameters = []
function removeElement(event, position) {
    swal({
        title: "¿Quieres borrar este par ordenado?",
        text: "Las coordenadas serán eliminadas "+position,
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
    const templateElement = (xvalue,yvalue, position) => {
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
            div.innerHTML = templateElement(form.coorX.value , form.coorY.value, index);            
            divElements.insertBefore(div, divElements.firstChild);
            form.reset();            
        } else {            
            swal("Datos incorrectos", "Ingresa las coordenadas adecuadamente", "error");
        }
    });

    btnCalculate.addEventListener("click",(evento)=>{        
        parameters = parameters.filter(element => element!=null);
        if(parameters.length != 0){
            const jsonDiv = document.getElementById("jsonArea");
            jsonDiv.innerHTML = JSON.stringify(parameters);
            divElements.innerHTML = "";
            parameters = [];
        }else{
            swal("Faltan Datos", "No ha ingresado ninguna coordenada", "error");
        }
    });

    // console.log(form)
    // console.log(divElements)
    // console.log(btnCalculate)
    // console.log(btnAdd)
})()