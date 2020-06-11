var seccionActual = ""

$('.btnMostrarGrupo').click(function() {
    // username=test%40gmail.com&password=123
    var clave = "clave=" + $(this).val()
    // console.log(clave)
    $.ajax({
        url: '/grupo',
        data: clave,
        type: 'POST',
        success: function(response) {
            console.log(response);
            // Datos de la seccion de detalles
            let grupo = response.grupo[0]
            document.getElementById('docente').innerHTML = grupo.docente
            document.getElementById('turno').innerHTML = grupo.turno
            document.getElementById('periodo').innerHTML = grupo.periodo
            document.getElementById('minmax').innerHTML = grupo.minmax
            document.getElementById('act').innerHTML = grupo.act
            document.getElementById('are').innerHTML = grupo.are

            // // Datos de la seccion de alumnos

            // console.log("response = " + response.grupos)
            console.log(response.alumnos)

            $('#tablaAlumnos').bootstrapTable('load', response.alumnos)

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