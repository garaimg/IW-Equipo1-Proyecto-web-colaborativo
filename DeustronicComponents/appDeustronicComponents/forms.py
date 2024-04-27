from django import forms
from .models import Producto, Componente


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class ComponenteForm(forms.ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'
