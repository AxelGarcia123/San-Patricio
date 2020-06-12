$("#btnGenerar").click(function() {
    console.log("hola")
    $.ajax({
        url: '/nomina',
        data: "",
        type: 'POST',
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
})