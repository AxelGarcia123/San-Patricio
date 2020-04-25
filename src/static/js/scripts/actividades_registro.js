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