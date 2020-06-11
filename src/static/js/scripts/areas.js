var seccionActual = ""

$('.btnMostrarArea').click(function() {
    // username=test%40gmail.com&password=123
    var clave = "clave=" + $(this).val()
    // console.log(clave)
    $.ajax({
        url: '/area',
        data: clave,
        type: 'POST',
        success: function(response) {
            console.log(response);
            // Datos de la seccion de detalles
            let area = response.area[0]
            document.getElementById('nombre').innerHTML = area.nombre
            document.getElementById('tipo').innerHTML = area.tipo
            document.getElementById('medidas').innerHTML = area.medidas
            document.getElementById('detallesArea').innerHTML = area.detalles

            // Datos de la seccion de grupos
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