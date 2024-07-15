from django.shortcuts import redirect, render
from django.http import HttpResponse

from dataManager.models import Usuario, Producto
import base64

# Views
# ---- RENDERIZADO ---- #
# Página | Inicio 
def pagIndex(request):
    return render(request, "index.html")

# Página | Nosotros
def pagAbout(request):
    return render(request, "about.html")

# Página | Contacto
def pagContact(request):
    return render(request, "contact.html")

# Página | Productos
def pagProducts(request):
    listaProductos = Producto.objects.all()
    return render(request, "products.html", {"productos": listaProductos})

# Página | Iniciar Sesión
def pagLogin(request):
    return render(request, "login.html")

# Página | Registrarse
def pagRegister(request):
    return render(request, "register.html")

# Página | Carrito
def pagCart(request):
    return render(request, "cart.html")





# ---- AGREGAR DATOS ---- #
# Registrar un usuario
def registrarUsuario(request):
    # Obtener datos del formulario de registro
    nombre = request.POST['inputUserName']
    apellido = request.POST['inputUserLastName']
    email = request.POST['inputUserEmail']
    clave1 = request.POST['inputUserPass1']
    clave2 = request.POST['inputUserPass2']
    
    # Si las claves ingresadas son iguales
    if clave1 == clave2:
        # Registrar datos en la tabla Usuario
        usuario = Usuario.objects.create(
            nombre = nombre,
            apellido = apellido,
            email = email,
            clave = clave1
        )
        
    return redirect('/registrarse')

    

# ---- VALIDACIONES ---- #
# Validar si el correo existe en la base de datos
def validarEmail(email):
    # Obtener todos los datos de la tabla Usuario
    listaUsuarios = Usuario.objects.all()

    # Por cada usuario en la tabla Usuario
    for usuario in listaUsuarios:
        if usuario.email == email:
            return true
        else:
            return false
        
# Validar si el correo y la contraseña coinciden