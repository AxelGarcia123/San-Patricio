var tablaEmpleados = $('#tablaEmpleados')
var tablaAlumnos = $('#tablaAlumnos')
var tablaMateriales = $('#tablaMateriales')

var btnSeleccionarPersona = document.getElementById('btnSeleccionarPersona')
var btnSeleccionarMaterial = document.getElementById('btnSeleccionarMaterial')

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
        clave = seleccionAlumno["1"]

    console.log(clave)

    // let clave = seleccion["1"]

    $("#persona").val(clave)

    $("#buscarPersonas").modal('hide')
})

////////////// MODAL DE MATERIALES //////////////

$("#buscarMaterial").click(() => { // Habilita o deshabilita el boton de seleccion al mostrar el modal
    let seleccionMateriales = tablaMateriales.bootstrapTable('getSelections')[0]

    if (seleccionMateriales != undefined) 
        $( "#btnSeleccionarMaterial" ).prop( "disabled", false )
    else
        $( "#btnSeleccionarMaterial" ).prop( "disabled", true )
})

$(tablaMateriales).on('click', 'tbody', () => { // Habilita o deshabilita el boton de seleccion dentro del modal
    let seleccionMateriales = tablaMateriales.bootstrapTable('getSelections')[0]

    if (seleccionMateriales != undefined) 
        $( "#btnSeleccionarMaterial" ).prop( "disabled", false )
    else    
        $( "#btnSeleccionarMaterial" ).prop( "disabled", true )
})

btnSeleccionarMaterial.addEventListener('click', () => { // Selecciona el material en el select, cierra el modal
    let seleccionMaterial = tablaMateriales.bootstrapTable('getSelections')[0]

    var clave = seleccionMaterial["1"]

    $("#material").val(clave)

    $("#buscarMateriales").modal('hide')
})