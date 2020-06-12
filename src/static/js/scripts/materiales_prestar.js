var $tablaSolicitudes = $("#tablaSolicitudes")

var btnSeleccionarSolicitud = document.getElementById('btnSeleccionarSolicitud')

////////////// MODAL DE SOLICITUDES //////////////

$("#buscarSolicitud").click(() => { // Habilita o deshabilita el boton de seleccion al mostrar el modal
    let seleccion = $tablaSolicitudes.bootstrapTable('getSelections')[0]

    if (seleccion != undefined) 
        $( "#btnSeleccionarSolicitud" ).prop( "disabled", false )
    else
        $( "#btnSeleccionarSolicitud" ).prop( "disabled", true )
})

$($tablaSolicitudes).on('click', 'tbody', () => { // Habilita o deshabilita el boton de seleccion dentro del modal
    let seleccion = $tablaSolicitudes.bootstrapTable('getSelections')[0]

    if (seleccion != undefined) 
        $( "#btnSeleccionarSolicitud" ).prop( "disabled", false )
    else    
        $( "#btnSeleccionarSolicitud" ).prop( "disabled", true )
})

btnSeleccionarSolicitud.addEventListener('click', () => { // Selecciona el material en el select, cierra el modal
    let seleccion = $tablaSolicitudes.bootstrapTable('getSelections')[0]
    let _clave = seleccion["1"]

    $("#solicitud").val(_clave)

    $("#buscarSolicitudes").modal('hide')

    let clave = "clave=" + _clave

    $.ajax({
        url: '/pSolicitud',
        data: clave,
        type: 'POST',
        success: function(response) {
            console.log(response);

            $('#tablaSolicitudMateriales').bootstrapTable('load', response.solicitudes)
        },
        error: function(error) {
            console.log(error);
        }
    });
})

////////////// GENERAR DATOS DE SOLICITUD //////////////



// $("#agregar").click(function() {
//     let material = $("#material").val()
//     let cantidad = $("#cantidad").val()
//     let html = "<tr>"
//         html += "<th scope='row'>" + contador  + "</th>"
//         html += "<td><input id='cantidadVal' name='cantidadVal' style='border:0;' readonly value=" + cantidad +  "></td>"
//         html += "<td><input id='materialVal' name='materialVal' style='border:0;' readonly value=" + material + "></td>"
//     html += "</tr>"
//     $tablaSolicitudes.append(html)
// })