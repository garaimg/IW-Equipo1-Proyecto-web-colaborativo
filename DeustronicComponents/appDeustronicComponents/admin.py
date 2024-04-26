from django.contrib import admin
from .models import Cliente, Producto, Componente, PedidoProducto, Pedido

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Componente)
admin.site.register(Pedido)
admin.site.register(PedidoProducto)
