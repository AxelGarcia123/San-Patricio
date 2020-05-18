var tablaEmpleados = $('#tablaEmpleados')
var tablaAlumnos = $('#tablaAlumnos')

var btnSeleccionarPersona = document.getElementById('btnSeleccionarPersona')

$("#buscarPersona").click(() => { // Habilita o deshabilita el boton de seleccion al mostrar el modal
    let seleccionEmpleados = tablaEmpleados.bootstrapTable('getSelections')[0]
    let seleccionAlumnos = tablaAlumnos.bootstrapTable('getSelections')[0]

    if (seleccionEmpleados != undefined || seleccionAlumnos != undefined) 
        $( "#btnSeleccionarPersona" ).prop( "disabled", false )
    else
        $( "#btnSeleccionarPersona" ).prop( "disabled", true )
})

$(tablaEmpleados).on('click', 'tbody', () => { // Habilita o deshabilita el boton de seleccion dentro del modal
    let seleccionEmpleados = tablaEmpleados.bootstrapTable('getSelections')[0]
    let seleccionAlumnos = tablaAlumnos.bootstrapTable('getSelections')[0]

    if (seleccionEmpleados != undefined || seleccionAlumnos != undefined) 
        $( "#btnSeleccionarPersona" ).prop( "disabled", false )
    else    
        $( "#btnSeleccionarPersona" ).prop( "disabled", true )
})

$(tablaAlumnos).on('click', 'tbody', () => { // Habilita o deshabilita el boton de seleccion dentro del modal
    let seleccionEmpleados = tablaEmpleados.bootstrapTable('getSelections')[0]
    let seleccionAlumnos = tablaAlumnos.bootstrapTable('getSelections')[0]

    if (seleccionEmpleados != undefined || seleccionAlumnos != undefined) 
        $( "#btnSeleccionarPersona" ).prop( "disabled", false )
    else    
        $( "#btnSeleccionarPersona" ).prop( "disabled", true )
})

btnSeleccionarPersona.addEventListener('click', () => { // Selecciona la persona en el select, cierra el modal
    let seleccionEmpleado = tablaEmpleados.bootstrapTable('getSelections')[0]
    let seleccionAlumno = tablaAlumnos.bootstrapTable('getSelections')[0]

    // console.log(seleccionEmpleado)
    // console.log(seleccionAlumno)

    var clave = 0

    if (seleccionEmpleado != undefined)
        clave = seleccionEmpleado["1"]
    else
        clave = seleccionAlumnos["1"]

    console.log(clave)

    // let clave = seleccion["1"]

    $("#persona").val(clave)

    $("#buscarPersonas").modal('hide')
})