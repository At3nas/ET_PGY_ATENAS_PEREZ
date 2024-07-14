from django.urls import path
from . import views

# URLS
urlpatterns = [
    path('', views.pagIndex),
    path('nosotros', views.pagAbout),
    path('contacto', views.pagContact),
    path('productos', views.pagProducts),
    path('iniciarSesion', views.pagLogin),
    path('registrarse', views.pagRegister),
    path('carrito', views.pagCart),
    path('registrarUsuario/', views.registrarUsuario),
]