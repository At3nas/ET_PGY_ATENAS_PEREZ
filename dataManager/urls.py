from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('dashboard/productos', views.dmProductos),
    path('dashboard/categoriaProducto', views.dmCategProd),
    path('dashboard/dctoProducto', views.dmDctoProd),
    path('agregarCategoria/', views.agregarCategoria),
    path('agregarDescuento/', views.agregarDescuento),
    path('edicionProducto/<id>', views.edicionProducto),
    path('eliminarProducto/<id>', views.eliminarProducto),
    path('agregarProducto/', views.agregarProducto),
    path('editarProducto/', views.editarProducto),
]