from django.contrib import admin
from .models import CategoriaProducto, Compra, Despacho, DetalleCompra, EstadoDespacho, Producto, Suscriptor, Usuario, DescuentoProducto

# Register your models here.
admin.site.register(CategoriaProducto)
admin.site.register(Compra)
admin.site.register(Despacho)
admin.site.register(DetalleCompra)
admin.site.register(EstadoDespacho)
admin.site.register(Producto)
admin.site.register(Suscriptor)
admin.site.register(Usuario)
admin.site.register(DescuentoProducto)