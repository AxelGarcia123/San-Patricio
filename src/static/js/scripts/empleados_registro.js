// control horarios

var data = $("#data").html()
var flag = true

$("#fijo").on('click', function () {
    flag = true
    $("#data").empty()
    $("#data").append(data)
})

$("#personalizado").on('click', function () {
    flag = false
    agregarDias()
})

$("input[name ='dia']").on('click', function () {
    if (!flag) {
        agregarDias() 
    }
})

function agregarDias() {
    var dias = []
    $.each($("input[name='dia']:checked"), function () {
        dias.push($(this).val())
    })

    var html = ''

    for (let i = 0; i < dias.length; i++) {
        html += "<h5 class='mt-3'>" + dias[i] + "</h5>"
        html += data
    }

    $("#data").empty()
    $("#data").append(html)
}