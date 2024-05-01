from django import forms
from .models import Producto, Componente, Cliente, Pedido, PedidoProducto


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


class ComponenteFormUpdate(forms.ModelForm):
    class Meta:
        model = Componente
        fields = ['modelo', 'marca']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class ClienteFormUpdate(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_empresa', 'direccion', 'telefono', 'email']


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cod_ref_ped', 'fecha', 'cliente']


class PedidoFormUpdate(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['fecha', 'cliente']


class PedidoProductoForm(forms.ModelForm):
    class Meta:
        model = PedidoProducto
        fields = ['pedido', 'producto', 'cantidad']


class PedidoProductoFormUpdate(forms.ModelForm):
    class Meta:
        model = PedidoProducto
        fields = ['pedido', 'producto', 'cantidad']
