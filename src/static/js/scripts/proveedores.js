var seccionActual = ""

$('.btnMostrar').click(function() {
    // username=test%40gmail.com&password=123
    var clave = "clave=" + $(this).val()
    // console.log(clave)
    $.ajax({
        url: '/proveedor',
        data: clave,
        type: 'POST',
        success: function(response) {
            console.log(response);
            // Datos de la seccion general
            document.getElementById('empresa').innerHTML = response.general[0].empresa
            document.getElementById('domicilio').innerHTML = response.general[0].domicilio
            document.getElementById('tel').innerHTML = response.general[0].tel
            // document.getElementById('descripcion').innerHTML = response.material[0].descripcion
            // document.getElementById('act').innerHTML = response.material[0].act

            
        },
        error: function(error) {
            console.log(error);
        }
    });

    document.getElementById('datos').removeAttribute('hidden')
    if (seccionActual != "") document.getElementById(seccionActual).setAttribute('hidden', 'true')
    document.getElementById('datosGenerales').removeAttribute('hidden')
    seccionActual = "datosGenerales"
});

$(".btnSeccion").click(function () {
    var seccionNueva = String( $(this).val() )
    document.getElementById(seccionActual).setAttribute('hidden', 'true')
    document.getElementById(seccionNueva).removeAttribute('hidden')
    seccionActual = seccionNueva
})

// $(document).on('click', '#btnInscribir', function () {
//     document.getElementById('contenidoFormInscripcion').removeAttribute('hidden')
// })

// $(document).on('click', '#btnGenerarFolio', function () {
//     $("#toastFolio").toast('show')
// })

// $(document).on('submit', '#formInscripcion', function (e) {
//     e.preventDefault()
//     // username=test%40gmail.com&password=123
//     var data = "fecha=" + $("#_fecha").val() + "&importe=" + $("#importe").val() + "&grupo=" + $("#grupo").val() + "&folio=" + $("#folio").text()
//     console.log(data)
//     $.ajax({
//         url: '/alumnoInscribir',
//         data: data,
//         type: 'POST',
//         success: function (response) {
//             console.log(response)

//             $("#toastFolio").toast('show')
//         },
//         error: function (error) {
//             console.log(error)   
//         }
//     })
// })

// $("#toastFolio").on('hidden.bs.toast', function () {
//     location.reload()
// })