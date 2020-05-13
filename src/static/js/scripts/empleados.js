$('.btnMostrarEmpleado').click(function() {
    // username=test%40gmail.com&password=123
    var clave = "clave=" + $(this).val()
    console.log(clave)
    $.ajax({
        url: '/empleado',
        data: clave,
        type: 'POST',
        success: function(response) {
            console.log(response);
            document.getElementById('resultadoh1').innerHTML = response.rfc
        },
        error: function(error) {
            console.log(error);
        }
    });
});