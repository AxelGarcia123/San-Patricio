var btnSeleccionarMaterial = document.getElementById('btnSeleccionarMaterial')
var btnSeleccionarProveedor = document.getElementById('btnSeleccionarProveedor')

var tablaMateriales = $('#tablaMateriales')
var tablaProveedores = $('#tablaProveedores')

////////////////////// CONTROL DE BUSQUEDA Y SELECCION DE MATERIAL //////////////////////

$("#buscarMaterial").click(() => { // Habilita o deshabilita el boton de seleccion al mostrar el modal
    let seleccion = tablaMateriales.bootstrapTable('getSelections')[0]

    if (seleccion != undefined) 
        $( "#btnSeleccionarMaterial" ).prop( "disabled", false )
    else
        $( "#btnSeleccionarMaterial" ).prop( "disabled", true )
})

$(tablaMateriales).on('click', 'tbody', () => { // Habilita o deshabilita el boton de seleccion dentro del modal
    let seleccion = tablaMateriales.bootstrapTable('getSelections')[0]

    if (seleccion != undefined) 
        $( "#btnSeleccionarMaterial" ).prop( "disabled", false )
    else    
        $( "#btnSeleccionarMaterial" ).prop( "disabled", true )
})

btnSeleccionarMaterial.addEventListener('click', () => { // Selecciona el material en el select, cierra el modal
    let seleccion = tablaMateriales.bootstrapTable('getSelections')[0]
    let clave = seleccion["1"]

    $("#material").val(clave)

    $("#buscarMateriales").modal('hide')
})

////////////////////// CONTROL DE BUSQUEDA Y SELECCION DE PROVEEDOR //////////////////////

$("#buscarProveedor").click(() => { // Habilita o deshabilita el boton de seleccion al mostrar el modal
    let seleccion = tablaProveedores.bootstrapTable('getSelections')[0]

    if (seleccion != undefined) 
        $( "#btnSeleccionarProveedor" ).prop( "disabled", false )
    else
        $( "#btnSeleccionarProveedor" ).prop( "disabled", true )
})

$(tablaProveedores).on('click', 'tbody', () => { // Habilita o deshabilita el boton de seleccion dentro del modal
    let seleccion = tablaProveedores.bootstrapTable('getSelections')[0]

    if (seleccion != undefined) 
        $( "#btnSeleccionarProveedor" ).prop( "disabled", false )
    else    
        $( "#btnSeleccionarProveedor" ).prop( "disabled", true )
})

btnSeleccionarProveedor.addEventListener('click', () => { // Selecciona el proveedor en el select, cierra el modal
    let seleccion = tablaProveedores.bootstrapTable('getSelections')[0]
    let clave = seleccion["1"]

    $("#proveedor").val(clave)

    $("#buscarProveedores").modal('hide')
})