# Create your models here.
from django.db import models
# Modelo que contiene la información de los clientes
from django.contrib.auth.hashers import make_password, check_password


class Cliente(models.Model):
    cif = models.CharField(max_length=100, primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=16)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        check = check_password(raw_password, self.password)
        print(check)
        return check

    def __str__(self):
        return f"{self.nombre_empresa}"

    class Meta:
        verbose_name_plural = "clientes"
        verbose_name = "cliente"
        ordering = ["-created"]


# Modelo que contiene la información de los pedidos
class Pedido(models.Model):
    cod_ref_ped = models.CharField(max_length=100, primary_key=True)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, default='en proceso')

    def __str__(self):
        return f"{self.cod_ref_ped}"

    class Meta:
        verbose_name_plural = "pedidos"
        verbose_name = "pedido"
        ordering = ["-created"]


# Modelo que contiene la información de los componentes
class Componente(models.Model):
    cod_ref_comp = models.CharField(max_length=100, primary_key=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.modelo}"

    class Meta:
        verbose_name_plural = "componentes"
        verbose_name = "componente"
        ordering = ["-created"]


# Modelo que contiene la información de los preductos
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
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = "productos"
        verbose_name = "producto"
        ordering = ["-created"]


# Modelo que contiene la información de los productos que tiene cada pedido asi como la cantidad de
# productos que se han solicitado en cada pedido cada pedido
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
