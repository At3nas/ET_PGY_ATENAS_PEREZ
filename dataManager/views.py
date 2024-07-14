from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import admin
from .models import CategoriaProducto, Compra, Despacho, DetalleCompra, EstadoDespacho, Producto, Suscriptor, Usuario

# Create your views here.

# ---- DATA MANAGER | VISTAS ---- #
# VISTA | DASHBOARD #
def dashboard(request):
   return render(request, "dashboard.html")

# VISTA | PRODUCTOS #
def dmProductos(request):
    listaProductos = Producto.objects.all()
    return render(request, "dmProductos.html", {"productos": listaProductos})

# VISTA | USUARIOS #
def dmUsuarios(request):
    listaUsuarios = Usuario.objects.all()
    return render(request, "dmUsuarios.html", {"usuarios": listaUsuarios})

# VISTA | COMPRAS #
def dmCompras(request):
    listaCompras = Compra.objects.all()
    return render(request, "dmCompras.html", {"compras": listaCompras})

# VISTA | CATEGORIA_PRODUCTOS #
def dmCategProd(request):
    listaCategoria = CategoriaProducto.objects.all()
    return render(request, "dmCategProd.html", {"categorias": listaCategoria})





# Renderiza la vista Edición de Producto
def edicionProducto(request, id):
    producto = Producto.objects.get(id_prod = id)
    return render(request, 'edicionProducto.html', {"producto": producto})

# Agrega datos a la tabla Productos
def agregarProducto(request):
   nombre = request.POST['inputName']
   stock = request.POST['inputStock']
   precio = request.POST['inputPrice']
   descuento = request.POST['inputDesc']

   producto=Producto.objects.create(
    nombre = nombre,
    stock = stock,
    precio = precio,
    descuento = descuento
   )

   return redirect('/dashboard')

# Elimina datos de la tabla Producto
def eliminarProducto(request, id):
    producto = Producto.objects.get(id_prod = id)
    producto.delete()

    return redirect('/dashboard')

# Edita datos de la tabla Producto
def editarProducto(request):
    id_prod = request.POST['inputId']
    nombre = request.POST['inputName']
    stock = request.POST['inputStock']
    precio = request.POST['inputPrice']
    descuento = request.POST['inputDesc']

    producto = Producto.objects.get(id_prod = id_prod)
    producto.nombre = nombre
    producto.stock = stock
    producto.precio = precio
    producto.descuento = descuento

    producto.save()

    return redirect('/dashboard')