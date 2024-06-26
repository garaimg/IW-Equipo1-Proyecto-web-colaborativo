"""
URL configuration for DeustronicComponents project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import *

# Grupo de urls para el correcto redireccionamiento de nuestro proyecto
urlpatterns = [
    # url de la página principal
    path('', IndexView.as_view(), name='index'),
    path('register/', Registro, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutRedirectView.as_view(), name='logout'),

    path('mail/', Send.as_view(), name='mail'),
    # urls para la gestión de productos
    path('producto/create/', ProductoCreateView.as_view(), name='crear_producto'),
    path('producto/<str:pk>/update/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/', ProductoListView.as_view(), name='lista_productos'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
    path('producto/<str:nombre>/detalle/', ProductoDetailView2.as_view(), name='detalle_producto2'),
    path('producto/<int:pk>/delete/', ProductoDeleteView.as_view(), name='eliminar_producto'),
    # urls para la gestión de componentes
    path('componentes/', ComponenteListView.as_view(), name='lista_componentes'),
    path('componente/<str:pk>', ComponenteDetailView.as_view(), name='detalle_componente'),
    path('componente/create/', ComponenteCreateView.as_view(), name='crear_componente'),
    path('componente/<str:pk>/update/', ComponenteUpdateView.as_view(), name='actualizar_componente'),
    path('componente/<int:pk>/delete/', ComponenteDeleteView.as_view(), name='eliminar_componente'),
    # urls para la gestión de clientes
    path('cliente/create/', ClienteCreateView.as_view(), name='crear_cliente'),
    path('cliente/', ClienteListView.as_view(), name='lista_clientes'),
    path('cliente/<str:pk>', ClienteDetailView.as_view(), name='detalle_cliente'),
    path('cliente/<str:pk>/update/', ClienteUpdateView.as_view(), name='actualizar_cliente'),
    path('cliente/<str:pk>/delete/', ClienteDeleteView.as_view(), name='eliminar_cliente'),
    # urls para la gestión de pedidos
    path('pedido/create/', PedidoCreateView.as_view(), name='crear_pedido'),
    path('pedido/<str:pk>/update/', PedidoUpdateView.as_view(), name='actualizar_pedido'),
    path('pedido/<str:pk>/delete/', PedidoDeleteView.as_view(), name='eliminar_pedido'),
    # urls para la gestión de los productos de cada pedido
    path('pedido_producto/create/', PedidoProductoCreateView.as_view(), name='crear_pedido_producto'),
    path('pedido_productos/', PedidoListView.as_view(), name='lista_pedido_productos'),
    path('pedido_producto/<str:pk>/', PedidoProductoDetailView.as_view(), name='detalle_pedido_producto'),
    path('pedido_producto/<str:pk>/update/', PedidoProductoUpdateView.as_view(), name='actualizar_pedido_producto'),
    path('pedido_producto/<str:pk>/delete/', PedidoProductoDeleteView.as_view(), name='eliminar_pedido_producto'),
    # url para la funcionalidad de ajax (actualizar estado del producto con solicitud post)
    path('update_pedido_estado/<str:pk>/', UpdatePedidoEstadoView.as_view(), name='update_pedido_estado'),
]
