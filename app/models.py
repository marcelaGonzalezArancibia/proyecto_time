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
    ESTADO_CHOICES = (
        ('creada', 'creada'),
        ('rectificada', 'Rectificada'),
          
    )
    ESTADOENTREGA_CHOICES = (
        ('por entregar', 'por entregar'),
        ('entregada', 'entregada'),
        ('rechazada', 'rechazada'), 
       
    )
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='creada')
    estadoentrega=models.CharField(max_length=20, choices=ESTADOENTREGA_CHOICES, default='por entregar')

   
    motivo_rechazo = models.TextField(blank=True, null=True)
    direccion_entrega = models.CharField(max_length=255, blank=True, null=True)
    rut_receptor = models.CharField(max_length=12, blank=True, null=True)
    foto_entrega = models.ImageField(upload_to='fotos_entrega/', blank=True, null=True)

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
            

class RechazoHistorial(models.Model):
    orden = models.ForeignKey(orden, related_name='rechazos', on_delete=models.CASCADE)
    motivo = models.TextField()
    

    def __str__(self):
        return f"Rechazo de {self.orden.id}"

