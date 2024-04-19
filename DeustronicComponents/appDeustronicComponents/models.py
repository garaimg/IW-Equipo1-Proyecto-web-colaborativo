from django.db import models

# Create your models here.
from django.db import models


class Cliente(models.Model):
    cif = models.CharField(max_length=100, primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField(max_length=15)
    email = models.EmailField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_empresa} ({self.cif})"

    class Meta:
        verbose_name_plural = "clientes"
        verbose_name = "cliente"
        ordering = ["-created"]


class Pedido(models.Model):
    cod_ref_ped = models.CharField(max_length=100, primary_key=True)
    fecha = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cod_ref_ped} ({self.fecha})"

    class Meta:
        verbose_name_plural = "pedidos"
        verbose_name = "pedido"
        ordering = ["-created"]


class Componente(models.Model):
    cod_ref_comp = models.CharField(max_length=100, primary_key=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cod_ref_comp} ({self.modelo})"

    class Meta:
        verbose_name_plural = "componentes"
        verbose_name = "componente"
        ordering = ["-created"]


class Producto(models.Model):
    cod_ref_prod = models.CharField(max_length=100, primary_key=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    componente = models.ManyToManyField(Componente)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.cod_ref_prod})"

    class Meta:
        verbose_name_plural = "productos"
        verbose_name = "producto"
        ordering = ["-created"]


class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.producto} ({self.cantidad})"

    class Meta:
        verbose_name_plural = "detalle pedidos"
        verbose_name = "detalle pedido"
        ordering = ["-created"]
