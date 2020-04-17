from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)


class Articulos(models.Model):
    nombre = models.CharField(max_length=40)
    seccion = models.CharField(max_length=40)
    precio = models.IntegerField()

    def __str__(self):

        return ('El nombre es %s y su precio es %s' %(self.nombre, self.precio))


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entrega = models.BooleanField()
