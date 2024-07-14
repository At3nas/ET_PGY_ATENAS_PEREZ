from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('dashboard/productos', views.dmProductos),
    path('dashboard/usuarios', views.dmUsuarios),
    path('dashboard/compras', views.dmCompras),
    path('dashboard/categoriaProductos', views.dmCategProd),
    path('edicionProducto/<id>', views.edicionProducto),
    path('eliminarProducto/<id>', views.eliminarProducto),
    path('agregarProducto/', views.agregarProducto),
    path('editarProducto/', views.editarProducto),
]