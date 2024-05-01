from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Producto, Componente, Cliente, Pedido, PedidoProducto
from .forms import ProductoForm, ComponenteForm, ClienteForm, PedidoForm, PedidoFormUpdate, ProductoFormUpdate, \
    ComponenteFormUpdate, ClienteFormUpdate, PedidoProductoForm, PedidoProductoFormUpdate


# Create your views here.
# UpdateView parecido a esto
class ProductoCreateView(View):

    def get(self, request):
        formulario = ProductoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/producto_create.html', context)

    def post(self, request):
        formulario = ProductoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(
                'index')
        return render(request, 'appDeustronicComponents/producto_create.html', {'formulario': formulario})


class IndexView(View):
    def get(self, request):
        return render(request, 'appDeustronicComponents/index.html')


class ProductoListView(ListView):
    model = Producto
    template_name = 'appDeustronicComponents/productos_list.html'
    context_object_name = 'productos'


class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'appDeustronicComponents/producto_detail.html'
    context_object_name = 'producto'

    def get_queryset(self):
        return Producto.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        producto = self.get_object()
        componentes = producto.componente.all()
        context['componentes'] = componentes
        return context


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoFormUpdate
    template_name = 'appDeustronicComponents/producto_update.html'
    success_url = reverse_lazy('index')

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


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'appDeustronicComponents/producto_confirm_delete.html'
    context_object_name = 'producto'
    success_url = reverse_lazy('index')


class ComponenteCreateView(View):

    def get(self, request):
        formulario = ComponenteForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/componente_create.html', context)

    def post(self, request):
        formulario = ComponenteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(
                'index')
        return render(request, 'appDeustronicComponents/componente_create.html', {'formulario': formulario})


class ComponenteListView(ListView):
    model = Componente
    template_name = 'appDeustronicComponents/componentes_list.html'
    context_object_name = 'componentes'


class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'appDeustronicComponents/componente_detail.html'
    context_object_name = 'componente'


class ComponenteUpdateView(UpdateView):
    model = Componente
    form_class = ProductoFormUpdate
    template_name = 'appDeustronicComponents/componente_update.html'
    success_url = reverse_lazy('index')

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


class ComponenteDeleteView(DeleteView):
    model = Componente
    template_name = 'appDeustronicComponents/componente_confirm_delete.html'
    context_object_name = 'componente'
    success_url = reverse_lazy('index')


class ClienteCreateView(View):

    def get(self, request):
        formulario = ClienteForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/cliente_create.html', context)

    def post(self, request):
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(
                'index')
        return render(request, 'appDeustronicComponents/cliente_create.html', {'formulario': formulario})


class ClienteListView(ListView):
    model = Cliente
    template_name = 'appDeustronicComponents/clientes_list.html'
    context_object_name = 'clientes'


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'appDeustronicComponents/cliente_detail.html'
    context_object_name = 'cliente'


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteFormUpdate
    template_name = 'appDeustronicComponents/cliente_update.html'
    success_url = reverse_lazy('index')

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
        formulario = ComponenteFormUpdate(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('detalle_cliente', pk=cliente.pk)
        else:
            return render(request, self.template_name, {'formulario': formulario})


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'appDeustronicComponents/cliente_confirm_delete.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('index')


class PedidoCreateView(View):
    def get(self, request):
        formulario = PedidoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/pedido_create.html', context)

    def post(self, request):
        formulario = PedidoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
        return render(request, 'appDeustronicComponents/pedido_create.html', {'formulario': formulario})


class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoFormUpdate
    template_name = 'appDeustronicComponents/pedido_update.html'
    success_url = reverse_lazy('index')

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
            return redirect('index')
        else:
            return render(request, self.template_name, {'formulario': formulario})


class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'appDeustronicComponents/pedido_confirm_delete.html'
    context_object_name = 'pedido'
    success_url = reverse_lazy('index')


class PedidoProductoCreateView(View):
    def get(self, request):
        formulario = PedidoProductoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustronicComponents/pedido_producto_create.html', context)

    def post(self, request):
        formulario = PedidoProductoForm(data=request.POST)
        if formulario.is_valid():
            pedido_producto = formulario.save()

            # Recalcular el precio total del pedido
            pedido = pedido_producto.pedido
            productos_del_pedido = PedidoProducto.objects.filter(pedido=pedido)
            precio_total_pedido = sum(prod.producto.precio * prod.cantidad for prod in productos_del_pedido)

            # Actualizar el precio total del pedido
            pedido.precio_total = precio_total_pedido
            pedido.save()

            return redirect('index')  # Redirige a la página principal o donde desees
        return render(request, 'appDeustronicComponents/pedido_producto_create.html', {'formulario': formulario})


class PedidoListView(ListView):
    model = Pedido
    template_name = 'appDeustronicComponents/pedido_producto_list.html'
    context_object_name = 'pedidos'


class PedidoProductoDetailView(DetailView):
    model = Pedido
    template_name = 'appDeustronicComponents/pedido_producto_detail.html'
    context_object_name = 'pedido'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pedido = self.get_object()

        # Obtener todos los productos asociados a este pedido
        productos_del_pedido = PedidoProducto.objects.filter(pedido=pedido)

        context['productos_del_pedido'] = productos_del_pedido
        return context


class PedidoProductoUpdateView(UpdateView):
    model = PedidoProducto
    form_class = PedidoProductoFormUpdate
    template_name = 'appDeustronicComponents/pedido_producto_update.html'
    success_url = reverse_lazy('lista_pedido_productos')

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
            formulario.save()
            return redirect('lista_pedido_productos')
        else:
            return render(request, self.template_name, {'formulario': formulario})


class PedidoProductoDeleteView(DeleteView):
    model = PedidoProducto
    template_name = 'appDeustronicComponents/pedido_producto_confirm_delete.html'
    context_object_name = 'pedidoproducto'
    success_url = reverse_lazy('lista_pedido_productos')
