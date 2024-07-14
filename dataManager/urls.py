from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('edicionProducto/<id>', views.edicionProducto),
    path('eliminarProducto/<id>', views.eliminarProducto),
    path('agregarProducto/', views.agregarProducto),
    path('editarProducto/', views.editarProducto),
]