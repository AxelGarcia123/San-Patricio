var seccionActual = ""

$('.btnMostrarEmpleado').click(function() {
    // username=test%40gmail.com&password=123
    var clave = "clave=" + $(this).val()
    // console.log(clave)
    $.ajax({
        url: '/empleado',
        data: clave,
        type: 'POST',
        success: function(response) {
            console.log(response);
            // Datos de la seccion general
            document.getElementById('nombre').innerHTML = response.personales[0].nombre
            document.getElementById('puesto').innerHTML = response.laborales[0].puesto
            document.getElementById('curp').innerHTML = response.personales[0].curp
            document.getElementById('domicilio').innerHTML = response.personales[0].domicilio
            document.getElementById('fnac').innerHTML = response.personales[0].fechanac
            document.getElementById('sexo').innerHTML = response.personales[0].genero
            document.getElementById('tel').innerHTML = response.personales[0].tel

            // Datos de la seccion laboral
            document.getElementById('rfc').innerHTML = response.laborales[0].rfc
            document.getElementById('puestoL').innerHTML = response.laborales[0].puesto
            document.getElementById('fechain').innerHTML = response.laborales[0].fechain
            document.getElementById('fechafin').innerHTML = response.laborales[0].fechafin

            // console.log(response.grupos)
            // console.log(typeof(response.grupos))
            // console.log(response.grupos[0])

            if (response.laborales[0].puesto == "Docente") {
                document.getElementById('_datosActividades').removeAttribute('hidden')
                document.getElementById('_datosGrupos').removeAttribute('hidden')

                var html = ""

                for (let i = 0; i < response.grupos.length; i++) {
                    html += "<tr id='tr-id-" + (i+1) + "' class='tr-class-" + (i + 1) + "'></tr>"
                    let grupo = response.grupos[i]
                    html += "<td>" + grupo.horaent + "-" + grupo.horasali + "</td>"
                    html += "<td>" + grupo.fechaini + "-" + grupo.fechafin + "</td>"
                    html += "<td>" + grupo.minalumnos + "/" + grupo.maxalumnos + "</td>"
                    html += "<td>" + grupo.act + "</td>"
                    html += "<td>" + grupo.are + "</td>"
                }

                document.getElementById('tablaActivos').innerHTML = html

            } else {
                document.getElementById('_datosActividades').setAttribute('hidden', 'true')
                document.getElementById('_datosGrupos').setAttribute('hidden', 'true')
            }

            // Datos de la seccion de horarios

            $("#tablaHorarios").bootstrapTable('load', response.horarios)

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