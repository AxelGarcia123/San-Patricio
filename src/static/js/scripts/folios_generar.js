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


// var folio = document.getElementById('folio')

// var numeros = "1234567890"

// function generarFolio() {
//     let folio_generado = ""
//     for (let i = 0; i < 11; i++) {
//         folio_generado += numeros.charAt(getRandom(0, numeros.length - 1))
//     }
//     folio.value = folio_generado
// }

// // min y max incluidos
// function getRandom(min, max) {
//     return Math.floor(Math.random() * (max - min + 1) ) + min;
// }

// generarFolio()