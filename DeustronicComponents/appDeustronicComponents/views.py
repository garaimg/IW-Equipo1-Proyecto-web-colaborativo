from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Producto, Componente
from .forms import ProductoForm


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


class ComponenteListView(ListView):
    model = Componente
    template_name = 'appDeustronicComponents/componentes_list.html'
    context_object_name = 'componentes'


class ComponenteDetailView(DetailView):
    model = Componente
    template_name = 'appDeustronicComponents/componente_detail.html'
    context_object_name = 'componente'
