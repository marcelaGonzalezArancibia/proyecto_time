from django.shortcuts import render, redirect
from .models import orden, ProductoOrden
from django.shortcuts import render, get_object_or_404
from .forms import OrdenForm, ProductoOrdenForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def crearorden(request):
    print('·············')
    print(request.POST)
    if request.method == 'POST':
        nombrevendedor = request.POST.get('nombrevendedor')
        rutvendedor = request.POST.get('rutvendedor')
        nombreempresa = request.POST.get('nombreempresa')
        direccionv = request.POST.get('direccionv')
        telefonov = request.POST.get('telefonov')
        correovendedor = request.POST.get('correovendedor')

        nombrecliente = request.POST.get('nombrecliente')
        rutcliente = request.POST.get('rutcliente')
        direccioncliente = request.POST.get('direccioncliente')
        correo = request.POST.get('correo')
        telefonoc = request.POST.get('telefonoc')

        valorNeto = float(request.POST.get('valorNeto'))
        iva = request.POST.get('iva')
        valorenvio = request.POST.get('valorenvio')
        TotalAPagar = float(request.POST.get('TotalAPagar'))

        orden_instance = orden.objects.create(
            nombrevendedor=nombrevendedor,
            rutvendedor=rutvendedor,
            nombreempresa=nombreempresa,
            direccionv=direccionv,
            telefonov=telefonov,
            correovendedor=correovendedor,
            nombrecliente=nombrecliente,
            rutcliente=rutcliente,
            direccioncliente=direccioncliente,
            correo=correo,
            telefonoc=telefonoc,
            valorNeto=valorNeto,
            iva=iva,
            valorenvio=valorenvio,
            TotalAPagar=TotalAPagar
        )

        productos = request.POST.getlist('producto')
        descripciones = request.POST.getlist('descripcion')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('preciounidad')
        totalproductos = request.POST.getlist('totalproducto')

        for producto, descripcion, cantidad, precio, totalproducto in zip(productos, descripciones, cantidades, precios, totalproductos):
            print('guardando producto')
            print(producto)
            ProductoOrden.objects.create(
                orden=orden_instance,
                producto=producto,
                descripcion=descripcion,
                cantidad=int(cantidad),
                preciounidad=int(precio),
                totalproducto=float(totalproducto)
            )
        return redirect('crearorden')  # Redirige a una página de éxito o la página que desees

    return render(request, 'crearorden.html')


def listadoorden(request):
    ordenes = orden.objects.all()  # Obtener todas las órdenes

   
    return render(request, 'listadoorden.html', {'ordenes': ordenes})

def detalleorden(request, orden_id):
    orden_instance = get_object_or_404(orden, pk=orden_id)
    productos = ProductoOrden.objects.filter(orden=orden_instance)
    return render(request, 'detalleorden.html', {'orden': orden_instance, 'productos': productos})



 
