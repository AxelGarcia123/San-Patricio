var seccionActual = ""

$('.btnMostrarSolicitud').click(function() {
    // username=test%40gmail.com&password=123
    var clave = "clave=" + $(this).val()
    // console.log(clave)
    $.ajax({
        url: '/solicitud',
        data: clave,
        type: 'POST',
        success: function(response) {
            console.log(response);
            // Datos de la seccion de detalles
            let solicitud = response.solicitud[0]
            document.getElementById('clave').innerHTML = solicitud.clave
            document.getElementById('solicitante').innerHTML = solicitud.solicitante
            document.getElementById('fecha').innerHTML = solicitud.fecha

            // Datos de la tabla de solicitudes
            $('#tablaSolicitud').bootstrapTable('load', response.solicitudes)

        },
        error: function(error) {
            console.log(error);
        }
    });

    document.getElementById('datos').removeAttribute('hidden')
    if (seccionActual != "") document.getElementById(seccionActual).setAttribute('hidden', 'true')
    document.getElementById('detalles').removeAttribute('hidden')
    seccionActual = "detalles"
});

$(".btnSeccion").click(function () {
    var seccionNueva = String( $(this).val() )
    document.getElementById(seccionActual).setAttribute('hidden', 'true')
    document.getElementById(seccionNueva).removeAttribute('hidden')
    seccionActual = seccionNueva
})