from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=45)
    direccion = models.CharField(max_length=60,verbose_name='La dirección')
    email = models.EmailField(blank=True,null=False)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre
    class Meta:
        ordering =  ['nombre']
    

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
    def __str__(self):

        return ('%s%s' %(self.id, self.fecha))
