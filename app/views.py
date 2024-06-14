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

    if request.method == 'POST':
        # Verificar si se presionó el botón de modificar
        if 'modificar' in request.POST:
            orden_id = request.POST.get('orden_id')
            orden_instance = get_object_or_404(orden, id=orden_id)
            orden_instance.estado = 'rectificada'  # Activar estado "Rectificada"
            orden_instance.save()
            return redirect('listadoorden')

    return render(request, 'listadoorden.html', {'ordenes': ordenes})

def detalleorden(request, orden_id):
    orden_instance = get_object_or_404(orden, pk=orden_id)
    productos = ProductoOrden.objects.filter(orden=orden_instance)
    return render(request, 'detalleorden.html', {'orden': orden_instance, 'productos': productos})




def modificar(request, orden_id):
    orden_instance = get_object_or_404(orden, id=orden_id)
    productos_instance = ProductoOrden.objects.filter(orden=orden_instance)

    if request.method == 'POST':
        orden_form = OrdenForm(request.POST, instance=orden_instance)
        productos_forms = []

        for producto_instance in productos_instance:
            producto_form = ProductoOrdenForm(
                request.POST,
                instance=producto_instance,
                prefix=f'producto-{producto_instance.id}'
            )
            productos_forms.append(producto_form)

        if orden_form.is_valid() and all(form.is_valid() for form in productos_forms):
            orden_instance = orden_form.save(commit=False)
            total_valor_neto = 0
            for form in productos_forms:
                producto = form.save(commit=False)
                producto.totalproducto = producto.cantidad * producto.preciounidad
                producto.save()
                total_valor_neto += producto.totalproducto

            orden_instance.valorNeto = total_valor_neto

            # Calcular TotalAPagar
            iva_porcentaje = float(orden_form.cleaned_data['iva'])
            valor_envio = float(orden_form.cleaned_data['valorenvio'])
            valor_iva = total_valor_neto * (iva_porcentaje / 100)
            total_pagar = total_valor_neto + valor_envio + valor_iva

            orden_instance.TotalAPagar = total_pagar
            
            # Verificar si se presionó el botón de modificar para activar el estado "Rectificada"
            if 'modificar' in request.POST:
                orden_instance.estado = 'rectificada'
            
            orden_instance.save()
            
            return redirect('detalleorden', orden_id=orden_instance.id)

    else:
        orden_form = OrdenForm(instance=orden_instance)
        productos_forms = [
            ProductoOrdenForm(
                instance=producto_instance,
                prefix=f'producto-{producto_instance.id}'
            ) for producto_instance in productos_instance
        ]

    return render(request, 'modificar.html', {
        'orden_form': orden_form,
        'productos_forms': productos_forms,
        'orden_instance': orden_instance,
    })

