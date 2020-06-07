var seccionActual = ""

$('.btnMostrarActividad').click(function() {
    // username=test%40gmail.com&password=123
    var clave = "clave=" + $(this).val()
    // console.log(clave)
    $.ajax({
        url: '/actividad',
        data: clave,
        type: 'POST',
        success: function(response) {
            console.log(response);
            // Datos de la seccion de detalles
            document.getElementById('nom').innerHTML = response.actividad[0].nom
            document.getElementById('tipo').innerHTML = response.actividad[0].tipo
            document.getElementById('descrip').innerHTML = response.actividad[0].descrip

            // Datos de la seccion de grupos

            console.log("response = " + response.grupos)
            console.log(response.grupos)

            $('#tablaGrupos').bootstrapTable('load', response.grupos)

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