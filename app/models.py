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