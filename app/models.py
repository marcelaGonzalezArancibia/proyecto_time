from django.db import models

# Create your models here.
class producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    marca = models.CharField(max_length=70)
    descripcion = models.TextField()
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class orden_compra(models.Model):
    codigo_orden = models.AutoField(primary_key=True)

    nombre_proveedor = models.CharField(max_length=70)
    rut_proveedor = models.CharField(max_length=9)
    direccion_empresa = models.CharField(max_length=70)
    telefono_proveedor=  models.CharField(max_length=8)
    correo_empresa = models.EmailField
    
    nombre_cliente = models.CharField(max_length=70)
    rut_cliente = models.CharField(max_length=9)
    direccion_cliente = models.CharField(max_length=70)
    telefono_cliente = models.CharField(max_length=8)
    correo_cliente = models.EmailField

    def __str__(self):
            return self.nombre_cliente
    