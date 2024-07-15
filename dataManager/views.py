from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import admin
from .models import CategoriaProducto, Compra, Despacho, DetalleCompra, EstadoDespacho, Producto, Suscriptor, Usuario, DescuentoProducto
import base64


# Create your views here.

# ---- DATA MANAGER | VISTAS ---- #
# VISTA | DASHBOARD #
def dashboard(request):
   return render(request, "dashboard.html")

# VISTA | PRODUCTOS #
def dmProductos(request):
    listaProductos = Producto.objects.all()
    listaCategorias = CategoriaProducto.objects.all()
    listaDescuentos = DescuentoProducto.objects.all()
    
    listas = {
        "productos": listaProductos, 
        "categorias": listaCategorias,
        "descuentos": listaDescuentos
    }

    return render(request, "dmProductos.html", listas)

# VISTA | CATEGORIA_PRODUCTOS #
def dmCategProd(request):
    listaCategoria = CategoriaProducto.objects.all()
    return render(request, "dmCategProd.html", {"categorias": listaCategoria})



def dmDctoProd(request):
    listaDescuentos = DescuentoProducto.objects.all()
    return render(request, "dmDctoProd.html", {"descuentos": listaDescuentos})


# Renderiza la vista Edición de Producto
def edicionProducto(request, id):
    producto = Producto.objects.get(id_prod = id)
    return render(request, 'edicionProducto.html', {"producto": producto})


# Agrega datos a la tabla Categoria_Producto
def agregarCategoria(request):
   id_categoria = request.POST['inputId']
   nombre_categoria = request.POST['inputName']

   categoria=CategoriaProducto.objects.create(
    id_categoria = id_categoria,
    nombre_categoria = nombre_categoria,
   )

   return redirect('/dashboard/categoriaProducto')

# Agrega datos a la tabla Descuento_Producto
def agregarDescuento(request):
#    id_dcto = request.POST['inputId']
   porc_dcto = request.POST['inputPorc']

   descuento=DescuentoProducto.objects.create(
    # id_dcto = id_dcto,
    porc_dcto = porc_dcto,
   )

   return redirect('/dashboard/dctoProducto')


# Agrega datos a la tabla Productos
def agregarProducto(request):
   if request.method == 'POST':      
    nombre = request.POST['inputName']
    stock = request.POST['inputStock']
    precio = request.POST['inputPrice']
    descripcion = request.POST['inputDesc']
    imagen = request.FILES['inputImg'].read()
    input_categ = request.POST['inputCateg']
    input_dcto = request.POST['inputDcto']

    # Busca las instancias de Categoria y Descuento ingresadas por el usuario
    id_categoria = CategoriaProducto.objects.get(id_categoria = input_categ)
    id_descuento = DescuentoProducto.objects.get(id_dcto = input_dcto)

    # Crea Producto
    producto=Producto.objects.create(
        nombre_producto = nombre,
        stock = stock,
        precio = precio,
        descripcion = descripcion,
        imagen = imagen,
        id_categoria = id_categoria,
        id_dcto = id_descuento
    )

    return redirect('/dashboard/productos')

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