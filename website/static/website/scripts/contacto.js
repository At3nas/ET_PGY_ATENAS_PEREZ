// Expresión que determina si el correo electrónico es válido
var isEmail = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;

$(document).ready(function () {
  // Al hacer click en el botón "Enviar" se validan los datos del formulario de Contacto
  $("#submitBtn").click(function () {

    // VALORES DE CADA INPUT //
    let nombre = $("#inputName").val();
    let email = $("#inputEmail").val();
    let motivo = $("#inputMotivo").val();
    let desc = $("#inputDesc").val();

    // VALIDAR NOMBRE
    if (nombre == "") {
      $("#inputName").addClass("is-invalid");
      return false;
    } else {
      $("#inputName").removeClass("is-invalid").addClass("is-valid");

      // VALIDAR CORREO
      if (email == "" || !isEmail.test(email)) {
        $("#inputEmail").addClass("is-invalid");
        return false;
      } else {
        $("#inputEmail").removeClass("is-invalid").addClass("is-valid");

        // VALIDAR MOTIVO
        if (motivo == 0) {
          $("#inputMotivo").addClass("is-invalid");
          return false;
        } else {
          $("#inputMotivo").removeClass("is-invalid").addClass("is-valid");

          // VALIDAR DESCRIPCION
          if (desc == "") {
            $("#inputDesc").addClass("is-invalid");
            return false;
          } else {
            $("#inputDesc").removeClass("is-invalid").addClass("is-valid");
          }
        }
      }
    }
  });
});
