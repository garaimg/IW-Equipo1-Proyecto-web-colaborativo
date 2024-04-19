from django.contrib import admin
from appDeustronicComponents.models import Cliente, Producto, Componente, PedidoProducto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Componente)
admin.site.register(PedidoProducto)
