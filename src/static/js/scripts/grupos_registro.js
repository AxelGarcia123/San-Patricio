(async function () {
    'use strict'
  
    window.addEventListener('load', async function () {  
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation')
  
      // Loop over them and prevent submission
      Array.prototype.filter.call(forms, async function (form) {
        form.addEventListener('submit', async function (event) {         
          if (form.checkValidity() === false) {
            event.preventDefault()
            event.stopPropagation()
          }
          form.classList.add('was-validated')
        }, false)
      })
  
    }, false)
}())

//////////

// LIMITAR FECHAS

// OBTENER ELEMENTOS
var fechaInicial = document.getElementById('fechaini')
var fechaFin = document.getElementById('fechafin')

// ESTABLECER LA FECHA ACTUAL EN fechaInicial
// LIMITAR FECHA MINIMA A LA FECHA ACTUAL, EN fechaFin
$(document).ready(() => {
    let date = new Date()
    let dia = date.getDate()
    let mes = (date.getMonth() < 10) ? "0" + (date.getMonth() + 1) : (date.getMonth() + 1)
    let anio = date.getFullYear()

    let fecha = anio + "-" + mes + "-" + dia
    fechaInicial.defaultValue = fecha // anio-mes-dia - 2020-04-24
    fechaFin.min = fecha
})

// LIMITAR FECHA MINIMA DE fechaFin AL ACTUALIZAR fechaInicio
fechaInicial.addEventListener('change', () => {
    fechaFin.min = fechaInicial.value
})

// FIN --- LIMITAR FECHAS