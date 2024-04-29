from django import forms
from .models import Producto, Componente, Cliente, Pedido


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoFormUpdate(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'categoria']

class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cod_ref_ped', 'fecha', 'cliente']


class PedidoFormUpdate(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha', 'cliente']
