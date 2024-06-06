from django.db import models

# Create your models here.
#-------vendedor
#nombre vendedor
#rut
#nombre empresa
#direccion
#telefono
#correo
#--------cliente
#nombre cliente
#rut
#direccion
#correo
#telefono
#------------orden
#idorden
#producto
#descripcion
#cantidad
#precio unidad
#precio total producto
#suma total productos
#iva
#envio
#precio total


class orden(models.Model):
    id = models.AutoField(primary_key=True) 
    nombrevendedor = models.CharField(max_length=90) 
    rutvendedor = models.CharField(max_length=9)
    nombreempresa = models.CharField(max_length=90)
    direccionv = models.CharField(max_length=90)
    telefonov = models.IntegerField(default=0)
    correovendedor = models.CharField(max_length=90)

    nombrecliente = models.CharField(max_length=90)
    rutcliente = models.CharField(max_length=9)
    direccioncliente = models.CharField(max_length=90)
    correo = models.CharField(max_length=90)
    telefonoc = models.IntegerField(default=0)

    valorNeto= models.IntegerField(default=0)
    iva = models.IntegerField(default=0)
    valorenvio = models.IntegerField(default=0)
    TotalAPagar = models.IntegerField(default=0)

    def __str__(self):
        return self.nombrevendedor
class ProductoOrden(models.Model):
    orden = models.ForeignKey(orden, on_delete=models.CASCADE, related_name='productos')
    producto = models.CharField(max_length=90)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    preciounidad = models.IntegerField()
    totalproducto = models.IntegerField(default=0)

    def __str__(self):
        return self.descripcion
            