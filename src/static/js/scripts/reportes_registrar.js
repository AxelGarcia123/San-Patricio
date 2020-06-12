var btnSeleccionarMaterial = document.getElementById('btnSeleccionarMaterial')

var tablaMateriales = $('#tablaMateriales')

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