from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, RedirectView
from .models import Producto, Componente, Cliente, Pedido, PedidoProducto
from .forms import ProductoForm, ComponenteForm, ClienteForm, PedidoForm, PedidoFormUpdate, ProductoFormUpdate, \
    ComponenteFormUpdate, ClienteFormUpdate, PedidoProductoForm, PedidoProductoFormUpdate


# Clase para la creación de los productos
class ProductoCreateView(View):

    @method_decorator(login_required)
    def get(self, request):
        formulario = ProductoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/producto_create.html', context)

    def post(self, request):
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(
                'lista_productos')
        return render(request, 'appDeustronicComponents/producto_create.html',
                      {'formulario': formulario})


# Clase para la visualización de la página principal
class IndexView(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'appDeustronicComponents/index.html')


# Clase para la visualización de la lista de todos los productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'appDeustronicComponents/productos_list.html'
    context_object_name = 'productos'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la visualización de la lista detallada de cierto producto
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'appDeustronicComponents/producto_detail.html'
    context_object_name = 'producto'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Producto.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.get_object()
        componentes = producto.componente.all()
        context['componentes'] = componentes
        return context


# Clase para la visualización de la lista detallada de cierto producto viniendo desde la vista detallada de los
# productos de un pedido
class ProductoDetailView2(DetailView):
    model = Producto
    template_name = 'appDeustronicComponents/producto_detail.html'
    context_object_name = 'producto'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        nombre_producto = self.kwargs['nombre']
        return get_object_or_404(Producto, nombre=nombre_producto)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.get_object()
        componentes = producto.componente.all()
        context['componentes'] = componentes
        return context


# Clase para la actualización de los detalles de cierto producto
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoFormUpdate
    template_name = 'appDeustronicComponents/producto_update.html'
    success_url = reverse_lazy('lista_productos')

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        producto = get_object_or_404(Producto, pk=pk)
        formulario = ProductoFormUpdate(instance=producto)
        context = {
            'formulario': formulario,
            'producto': producto
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        producto = get_object_or_404(Producto, pk=pk)
        formulario = ProductoFormUpdate(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_producto', pk=producto.pk)
        else:
            return render(request, self.template_name, {'formulario': formulario})


# Clase para la eliminación de cierto producto
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'appDeustronicComponents/producto_confirm_delete.html'
    context_object_name = 'producto'
    success_url = reverse_lazy('lista_productos')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la creación de los componentes
class ComponenteCreateView(View):

    @method_decorator(login_required)
    def get(self, request):
        formulario = ComponenteForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/componente_create.html', context)

    def post(self, request):
        formulario = ComponenteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(
                'lista_componentes')
        return render(request, 'appDeustronicComponents/componente_create.html', {'formulario': formulario})


# Clase para la visualización de la lista de todos los componentes
class ComponenteListView(ListView):
    model = Componente
    template_name = 'appDeustronicComponents/componentes_list.html'
    context_object_name = 'componentes'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la visualización de la lista detallada de cierto componente
class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'appDeustronicComponents/componente_detail.html'
    context_object_name = 'componente'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la atualización de cierto componente
class ComponenteUpdateView(UpdateView):
    model = Componente
    form_class = ProductoFormUpdate
    template_name = 'appDeustronicComponents/componente_update.html'
    success_url = reverse_lazy('lista_componentes')

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        componente = get_object_or_404(Componente, pk=pk)
        formulario = ComponenteFormUpdate(instance=componente)
        context = {
            'formulario': formulario,
            'producto': componente
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        componente = get_object_or_404(Componente, pk=pk)
        formulario = ComponenteFormUpdate(request.POST, instance=componente)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_componente', pk=componente.pk)
        else:
            return render(request, self.template_name, {'formulario': formulario})


# Clase para la eliminación de cierto componente
class ComponenteDeleteView(DeleteView):
    model = Componente
    template_name = 'appDeustronicComponents/componente_confirm_delete.html'
    context_object_name = 'componente'
    success_url = reverse_lazy('lista_componentes')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la creación de clientes
class ClienteCreateView(View):

    @method_decorator(login_required)
    def get(self, request):
        formulario = ClienteForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/cliente_create.html', context)

    def post(self, request):
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(
                'lista_clientes')
        return render(request, 'appDeustronicComponents/cliente_create.html', {'formulario': formulario})


# Clase para la visualización de la lista de todos los clientes
class ClienteListView(ListView):
    model = Cliente
    template_name = 'appDeustronicComponents/clientes_list.html'
    context_object_name = 'clientes'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la visualización de la lista detallada de cierto cliente
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'appDeustronicComponents/cliente_detail.html'
    context_object_name = 'cliente'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la actualización de cierto cliente
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteFormUpdate
    template_name = 'appDeustronicComponents/cliente_update.html'
    success_url = reverse_lazy('lista_clientes')

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        cliente = get_object_or_404(Cliente, pk=pk)
        formulario = ClienteFormUpdate(instance=cliente)
        context = {
            'formulario': formulario,
            'producto': cliente
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        cliente = get_object_or_404(Cliente, pk=pk)
        formulario = ClienteFormUpdate(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_cliente', pk=cliente.pk)
        else:
            return render(request, self.template_name, {'formulario': formulario})


# Clase para la eliminación de cierto cliente
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'appDeustronicComponents/cliente_confirm_delete.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('lista_clientes')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la cración de los pedidos
class PedidoCreateView(View):

    @method_decorator(login_required)
    def get(self, request):
        formulario = PedidoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/pedido_create.html', context)

    def post(self, request):
        formulario = PedidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('crear_pedido_producto')
        return render(request, 'appDeustronicComponents/pedido_create.html', {'formulario': formulario})


# Clase para la actualización de la información de cierto pedido
class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoFormUpdate
    template_name = 'appDeustronicComponents/pedido_update.html'
    success_url = reverse_lazy('lista_pedido_productos')

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        pedido = get_object_or_404(Pedido, pk=pk)
        formulario = PedidoFormUpdate(instance=pedido)
        context = {
            'formulario': formulario,
            'pedido': pedido
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        pedido = get_object_or_404(Pedido, pk=pk)
        formulario = PedidoFormUpdate(request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            return redirect('lista_pedido_productos')
        else:
            return render(request, self.template_name, {'formulario': formulario})


# Clase para la eliminación de cierto pedido
class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'appDeustronicComponents/pedido_confirm_delete.html'
    context_object_name = 'pedido'
    success_url = reverse_lazy('lista_pedido_productos')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la creación del producto que compone un pedido, guardando de uno en uno el producto con el pedido al que
# pertenece, haciendo que haya una entrada en el modelo por cada producto en un pedido
class PedidoProductoCreateView(View):

    @method_decorator(login_required)
    def get(self, request):
        formulario = PedidoProductoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/pedido_producto_create.html', context)

    def post(self, request):
        formulario = PedidoProductoForm(data=request.POST)
        if formulario.is_valid():
            pedido_producto = formulario.save()

            pedido = pedido_producto.pedido
            productos_del_pedido = PedidoProducto.objects.filter(pedido=pedido)
            precio_total_pedido = sum(prod.producto.precio * prod.cantidad for prod in productos_del_pedido)

            pedido.precio_total = precio_total_pedido
            pedido.save()

            return redirect('lista_pedido_productos')
        return render(request, 'appDeustronicComponents/pedido_producto_create.html', {'formulario': formulario})


# Clase para la visualización de la lista de todos los pedidos
class PedidoListView(ListView):
    model = Pedido
    template_name = 'appDeustronicComponents/pedido_producto_list.html'
    context_object_name = 'pedidos'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


# Clase para la visualización de la lista detallada de cierto pedido, donde se incluyen los productos que le han sido
# añadidos
class PedidoProductoDetailView(DetailView):
    model = Pedido
    template_name = 'appDeustronicComponents/pedido_producto_detail.html'
    context_object_name = 'pedido'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedido = self.get_object()

        productos_del_pedido = PedidoProducto.objects.filter(pedido=pedido)

        context['productos_del_pedido'] = productos_del_pedido
        return context


# Clase para la actualización de la información de cierto producto, permitiéndole cambiar la información del modelo

# Pedido-Producto. Esta información sería el pedido al que pertenece, el producto a comprar y la cantidad de productos
# que quiere
class PedidoProductoUpdateView(UpdateView):
    model = PedidoProducto
    form_class = PedidoProductoFormUpdate
    template_name = 'appDeustronicComponents/pedido_producto_update.html'
    success_url = reverse_lazy('lista_pedido_productos')

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        pedidoproducto = get_object_or_404(PedidoProducto, pk=pk)
        formulario = PedidoProductoFormUpdate(instance=pedidoproducto)
        context = {
            'formulario': formulario,
            'pedido': pedidoproducto
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        pedidoproducto = get_object_or_404(PedidoProducto, pk=pk)
        formulario = PedidoProductoFormUpdate(request.POST, instance=pedidoproducto)
        if formulario.is_valid():
            pedido_producto = formulario.save()

            pedido = pedido_producto.pedido
            productos_del_pedido = PedidoProducto.objects.filter(pedido=pedido)
            precio_total_pedido = sum(prod.producto.precio * prod.cantidad for prod in productos_del_pedido)

            pedido.precio_total = precio_total_pedido
            pedido.save()
            return redirect('lista_pedido_productos')
        else:
            return render(request, self.template_name, {'formulario': formulario})


# Clase para la eliminación de cierto producto en cierto pedido
class PedidoProductoDeleteView(DeleteView):
    model = PedidoProducto
    template_name = 'appDeustronicComponents/pedido_producto_confirm_delete.html'
    context_object_name = 'pedidoproducto'
    success_url = reverse_lazy('lista_pedido_productos')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        pedidoproducto = get_object_or_404(PedidoProducto, pk=pk)
        pedido = pedidoproducto.pedido

        pedidoproducto.delete()

        productos_del_pedido = PedidoProducto.objects.filter(pedido=pedido)
        precio_total_pedido = sum(prod.producto.precio * prod.cantidad for prod in productos_del_pedido)

        pedido.precio_total = precio_total_pedido
        pedido.save()

        return redirect('lista_pedido_productos')


class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


def Registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class UpdatePedidoEstadoView(View):

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if request.content_type == 'application/json':
            try:
                # Obtener los datos enviados en la solicitud
                data = json.loads(request.body)
                pedido_id = data.get('pedido_id')
                nuevo_estado = data.get('estado')

                # Actualizar el estado del pedido
                pedido = get_object_or_404(Pedido, pk=pedido_id)
                pedido.estado = nuevo_estado
                pedido.save()

                return JsonResponse({'success': True, 'estado': pedido.estado})
            except json.JSONDecodeError:
                return JsonResponse({'success': False, 'error': 'Invalid JSON'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid request'})


class Send(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'appDeustronicComponents/mail.html')

    def post(self, request):
        email = request.POST.get('email')

        template = get_template('appDeustronicComponents/email-order-success.html')

        # Se renderiza el template y se envias parametros
        content = template.render({'email': email})

        # Se crea el correo (titulo, mensaje, emisor, destinatario)
        msg = EmailMultiAlternatives(
            'Gracias por tu compra',
            'Hola, te enviamos un correo con tu factura',
            settings.EMAIL_HOST_USER,
            [email]
        )

        msg.attach_alternative(content, 'text/html')
        msg.send()

        messages.success(request, 'Te has suscrito a la newsletter correctamente')

        return render(request, 'appDeustronicComponents/mail.html')
