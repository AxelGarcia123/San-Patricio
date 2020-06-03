var seccionActual = ""

$('.btnMostrar').click(function() {
    // username=test%40gmail.com&password=123
    var clave = "clave=" + $(this).val()
    var estaInscrito = $(this).hasClass("inscrito")
    // console.log(clave)

    $.ajax({
        url: '/alumno',
        data: clave,
        type: 'POST',
        success: function(response) {
            // console.log(response);
            // Datos de la seccion general
            document.getElementById('nombre').innerHTML = response.personales[0].nombre
            // document.getElementById('puesto').innerHTML = response.laborales[0].puesto
            document.getElementById('curp').innerHTML = response.personales[0].curp
            document.getElementById('domicilio').innerHTML = response.personales[0].domicilio
            document.getElementById('fnac').innerHTML = response.personales[0].fechanac
            document.getElementById('sexo').innerHTML = response.personales[0].genero
            document.getElementById('tel').innerHTML = response.personales[0].tel

            // Datos de la seccion academica
            document.getElementById('estatura').innerHTML = response.alumno[0].estatura
            document.getElementById('peso').innerHTML = response.alumno[0].peso

            // console.log("grupos = " + response.grupos)

            // Datos de la sección de inscripción

            if (estaInscrito) {
                document.getElementById('btnDatosAcademicos').removeAttribute('hidden')


            } else {
                document.getElementById('btnDatosAcademicos').setAttribute('hidden', 'true')

                var html = ""

                if (response.folio.length > 0) {
                    let folio = response.folio[0]
                    html += "<div class='row'>"
                        html += "<div class='col-md-12' >"
                            html += "<div class='row'>"
                                html += "<div class='col-md-12 d-flex justify-content-between'>"
                                    html += "<h5 class='font-weight-bold'>Realizar inscripcion</h5><button class='btnEditar btn rounded-pill font-weight-bold px-3' id='btnInscribir'>Abrir formulario</button>"
                                html += "</div>"
                            html += "</div>"
                        html += "</div>"

                        html += "<div class='col-md-12' id='contenidoFormInscripcion' hidden>"
                            html += "<form class='needs-validation' id='formInscripcion' method=''>"

                                html += "<div class='row'>"
                                    html += "<div class='col-md-8'>"
                                        html += "<label for='grupo'>Grupo</label>"
                                        html += "<input type='text' class='form-control' id='grupo' name='grupo' placeholder='' value='' required disabled>"

                                        html += "<div class='invalid-feedback'>Elija un grupo válido.</div>"
                                    html += "</div>"

                                    html += "<div class='col-md-4 d-flex align-items-end justify-content-end'>"
                                        html += "<button type='button' class='btn btn-primary w-100' id='btnElegirGrupo' name='btnElegirGrupo' value='' data-toggle='modal' data-target='#buscarGrupos'>Elegir grupo</button>"
                                    html += "</div>"
                                html += "</div>"

                                html += "<div class='row'>"
                                    html += "<div class='col-md-12'>"
                                        html += "<label for='_fecha'>Fecha</label>"
                                        html += "<input type='date' class='form-control' id='_fecha' name='_fecha' placeholder='' value='' required autofocus>"

                                        html += "<div class='invalid-feedback'>Ingrese una fecha válida.</div>"
                                    html += "</div>"
                                html += "</div>"

                                html += "<div class='row'>"
                                    html += "<div class='col-md-12'>"
                                        html += "<label for='importe'>Importe</label>"
                                        html += "<input type='number' class='form-control' id='importe' name='importe' placeholder='' value='' required>"

                                        html += "<div class='invalid-feedback'>Ingrese un importe válido.</div>"
                                    html += "</div>"
                                html += "</div>"

                                // Extra
                                html += "<input type='number' id='_folio' name='_folio' value='" + folio[0] + "' hidden disabled>"

                                html += "<div class='row'>"
                                    html += "<div class='col-md-12 d-flex justify-content-end'>"
                                        html += "<button type='submit' class='mt-3 botones btn btn-lg mr-2 rounded-pill px-5' id='_btAceptar'>Inscribir</button>"
                                    html += "</div>"
                                html += "</div>"

                            html += "</form>"
                        html += "</div>"
                    html += "</div>"

                    html += "<hr>"

                    html += "<div class='row'>"
                        html += "<div class='col-md-12'>"
                            html += "<div class='row'>"
                                html += "<div class='col-md-12 d-flex justify-content-between'>"
                                    html += " <h5 class='font-weight-bold'>Folio</h5><button class='btnEditar btn rounded-pill font-weight-bold px-3'>Editar</button>"
                                html += "</div>"
                            html += "</div>"
                        html += "</div>"

                        html += "<div class='col-md-12'>"
                            html += "<div class='row pt-2'><div class='col-md-12'><h5 class='text-muted' id='folio'>" + folio[0] + "</h5></div></div>"
                        html += "</div>"
                    html += "</div>"

                    html += "<hr>"

                    html += "<div class='row'>"
                        html += "<div class='col-md-12'>"
                            html += "<div class='row'>"
                                html += "<div class='col-md-12 d-flex justify-content-between'>"
                                    html += " <h5 class='font-weight-bold'>Fecha</h5><button class='btnEditar btn rounded-pill font-weight-bold px-3'>Editar</button>"
                                html += "</div>"
                            html += "</div>"
                        html += "</div>"

                        html += "<div class='col-md-12'>"
                            html += "<div class='row pt-2'><div class='col-md-12'><h5 class='text-muted' id='fecha'>" + folio[1] + "</h5></div></div>"
                        html += "</div>"
                    html += "</div>"

                    html += "<hr>"

                    html += "<div class='row'>"
                        html += "<div class='col-md-12'>"
                            html += "<div class='row'>"
                                html += "<div class='col-md-12 d-flex justify-content-between'>"
                                    html += " <h5 class='font-weight-bold'>Costo</h5><button class='btnEditar btn rounded-pill font-weight-bold px-3'>Editar</button>"
                                html += "</div>"
                            html += "</div>"
                        html += "</div>"

                        html += "<div class='col-md-12'>"
                            html += "<div class='row pt-2'><div class='col-md-12'><h5 class='text-muted' id='costo'>$" + folio[2] + "</h5></div></div>"
                        html += "</div>"
                    html += "</div>"

                    html += "<hr>"

                    html += "<div class='row'>"
                        html += "<div class='col-md-12'>"
                            html += "<div class='row'>"
                                html += "<div class='col-md-12 d-flex justify-content-between'>"
                                    html += " <h5 class='font-weight-bold'>Actividad</h5><button class='btnEditar btn rounded-pill font-weight-bold px-3'>Editar</button>"
                                html += "</div>"
                            html += "</div>"
                        html += "</div>"

                        html += "<div class='col-md-12'>"
                            html += "<div class='row pt-2'><div class='col-md-12'><h5 class='text-muted' id='actividad'>" + folio[5] + "</h5></div></div>"
                        html += "</div>"
                    html += "</div>"

                    html += "<hr>"

                    // html += "<div class='row'>"
                    //     html += "<div class='col-md-12' >"
                    //         html += "<div class='row'>"
                    //             html += "<div class='col-md-12 d-flex justify-content-between'>"
                    //                 html += "<h5 class='font-weight-bold'>Realizar inscripcion</h5><button class='btnEditar btn rounded-pill font-weight-bold px-3' id='btnInscribir'>Abrir formulario</button>"
                    //             html += "</div>"
                    //         html += "</div>"
                    //     html += "</div>"

                    //     html += "<div class='col-md-12' id='contenidoFormInscripcion' hidden>"
                    //         html += "<form class='needs-validation' id='formInscripcion' method=''>"

                    //             html += "<div class='row'>"
                    //                 html += "<div class='col-md-8'>"
                    //                     html += "<label for='grupo'>Grupo</label>"
                    //                     html += "<input type='text' class='form-control' id='grupo' name='grupo' placeholder='' value='' required>"

                    //                     html += "<div class='invalid-feedback'>Elija un grupo válido.</div>"
                    //                 html += "</div>"

                    //                 html += "<div class='col-md-4 d-flex align-items-end justify-content-end'>"
                    //                     html += "<button type='button' class='btn btn-primary w-100' id='btnElegirGrupo' name='btnElegirGrupo' value=''>Elegir grupo</button>"
                    //                 html += "</div>"
                    //             html += "</div>"

                    //             html += "<div class='row'>"
                    //                 html += "<div class='col-md-12'>"
                    //                     html += "<label for='_fecha'>Fecha</label>"
                    //                     html += "<input type='date' class='form-control' id='_fecha' name='_fecha' placeholder='' value='' required autofocus>"

                    //                     html += "<div class='invalid-feedback'>Ingrese una fecha válida.</div>"
                    //                 html += "</div>"
                    //             html += "</div>"

                    //             html += "<div class='row'>"
                    //                 html += "<div class='col-md-12'>"
                    //                     html += "<label for='importe'>Importe</label>"
                    //                     html += "<input type='number' class='form-control' id='importe' name='importe' placeholder='' value='' required>"

                    //                     html += "<div class='invalid-feedback'>Ingrese un importe válido.</div>"
                    //                 html += "</div>"
                    //             html += "</div>"

                    //             html += "<div class='row'>"
                    //                 html += "<div class='col-md-12 d-flex justify-content-end'>"
                    //                     html += "<button type='submit' class='mt-3 botones btn btn-lg mr-2 rounded-pill px-5' id='_btAceptar'>Inscribir</button>"
                    //                 html += "</div>"
                    //             html += "</div>"

                    //         html += "</form>"
                    //     html += "</div>"
                    // html += "</div>"

                } else {

                    html += "<h5 class='font-weight-bold'>El alumno no está inscrito.</h5>"
                    html += "<h5 class='font-weight-bold'>Haga clic en el botón Generar folio para generar un folio.</h5>"
                    html += "<h5 class='font-weight-bold'>Generar folio</h5><button class='btnEditar btn rounded-pill font-weight-bold px-3' id='btnGenerarFolio'>Generar folio</button>"
                  
                }

                document.getElementById('contenidoInscripcion').innerHTML = html

            }
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

$(document).on('click', '#btnInscribir', function () { // Abre el formulario para inscribir alumno
    document.getElementById('contenidoFormInscripcion').removeAttribute('hidden')
})

// var renglonesOcultos = false
$(document).on('click', '#btnElegirGrupo', function () {
    $("#tablaGrupos tbody tr").toggle(true)
    var act = $("#actividad").text()
    $("#tablaGrupos tbody tr").not( ".act"+ act ).toggle(false)
})

$("#buscarGrupos").click(() => { // Habilita o deshabilita el boton de seleccion al mostrar el modal
    let seleccion = $("#tablaGrupos").bootstrapTable('getSelections')[0]

    if (seleccion != undefined) 
        $( "#btnSeleccionarGrupo" ).prop( "disabled", false )
    else
        $( "#btnSeleccionarGrupo" ).prop( "disabled", true )
})

$("#tablaGrupos").on('click', 'tbody', () => { // Habilita o deshabilita el boton de seleccion dentro del modal
    let seleccion = $("#tablaGrupos").bootstrapTable('getSelections')[0]

    if (seleccion != undefined) 
        $( "#btnSeleccionarGrupo" ).prop( "disabled", false )
    else    
        $( "#btnSeleccionarGrupo" ).prop( "disabled", true )
})

document.getElementById('btnSeleccionarGrupo').addEventListener('click', () => { // Selecciona el material en el select, cierra el modal
    let seleccion = $("#tablaGrupos").bootstrapTable('getSelections')[0]
    let clave = seleccion["1"]

    $("#grupo").val(clave)

    $("#buscarGrupos").modal('hide')
})

$(document).on('click', '#btnGenerarFolio', function () {
    $("#toastFolio").toast('show')
})

// $(document).on('click', '#_btAceptar', function (e) {
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

//             $("#toastInsc").toast('show')
//         },
//         error: function (error) {
//             console.log(error)   
//         }
//     })
// })

$(document).on('submit', '#formInscripcion', function (e) {
    e.preventDefault()
    // username=test%40gmail.com&password=123
    var data = "fecha=" + $("#_fecha").val() + "&importe=" + $("#importe").val() + "&grupo=" + $("#grupo").val() + "&folio=" + $("#folio").text()
    console.log(data)
    $.ajax({
        url: '/alumnoInscribir',
        data: data,
        type: 'POST',
        success: function (response) {
            console.log(response)

            $("#toastInsc").toast('show')
        },
        error: function (error) {
            console.log(error)   
        }
    })
})

$("#toastInsc").on('hidden.bs.toast', function () {
    location.reload()
})