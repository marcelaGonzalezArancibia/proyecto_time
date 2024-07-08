from django.shortcuts import render, redirect
from .models import orden, ProductoOrden,RechazoHistorial
from django.shortcuts import render, get_object_or_404
from .forms import OrdenForm, ProductoOrdenForm,EntregaForm
from .forms import ProductoOrdenFormSet

from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import View
from xhtml2pdf import pisa
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO
##se intala para pdf y gota de agua pip install xhtml2pdf reportlab
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

def rectificacion(request, orden_id):
    orden_instance = get_object_or_404(orden, id=orden_id)

    if request.method == 'POST':
        orden_form = OrdenForm(request.POST, instance=orden_instance)
        formset = ProductoOrdenFormSet(request.POST, instance=orden_instance)

        if orden_form.is_valid() and formset.is_valid():
            orden_form.save()
            formset.save()
            return redirect('detalleorden', orden_id=orden_instance.id)
    else:
        orden_form = OrdenForm(instance=orden_instance)
        formset = ProductoOrdenFormSet(instance=orden_instance)

    return render(request, 'rectificacion.html', {'orden_form': orden_form, 'formset': formset})

def entrega(request, orden_id):
    orden_obj = get_object_or_404(orden, id=orden_id)

    if request.method == 'POST':
        form = EntregaForm(request.POST, request.FILES, instance=orden_obj)
        if form.is_valid():
            if form.cleaned_data['estadoentrega'] == 'rechazada':
                motivo = form.cleaned_data.get('motivo_rechazo', '')
                RechazoHistorial.objects.create(orden=orden_obj, motivo=motivo)
            form.save()
            return redirect('listadoorden')
    else:
        form = EntregaForm(instance=orden_obj)
        
    return render(request, 'entrega.html', {'form': form, 'orden': orden_obj})


class DetalleOrdenPDF(View):
    def get(self, request, *args, **kwargs):
        # Obtener la orden y los productos
        orden_id = kwargs.get('orden_id')
        orden_instance = orden.objects.get(pk=orden_id)
        productos = ProductoOrden.objects.filter(orden=orden_instance)

        # Renderizar la plantilla con los datos
        template_path = 'detalleorden.html'
        context = {'orden': orden_instance, 'productos': productos}
        template = get_template(template_path)
        html = template.render(context)

        # Crear un objeto HttpResponse con el contenido PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="detalle_orden.pdf"'

        # Crear un buffer para almacenar el PDF generado por xhtml2pdf
        buffer = BytesIO()
        pisa_status = pisa.CreatePDF(html, dest=buffer, encoding='utf-8')

        if pisa_status.err:
            return HttpResponse('Error al generar PDF: %s' % html)

        # Mueve el puntero del buffer al inicio
        buffer.seek(0)

        # Si la orden está anulada, añade la marca de agua
        if orden_instance.estadoentrega == 'anulada':
            # Crear un nuevo buffer para el PDF final
            final_buffer = BytesIO()

            # Leer el contenido del PDF generado por xhtml2pdf
            pdf_reader = PdfReader(buffer)
            pdf_writer = PdfWriter()

            # Crear la marca de agua usando reportlab
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]

                packet = BytesIO()
                can = canvas.Canvas(packet, pagesize=letter)
                can.setFont("Helvetica-Bold", 50)
                can.setFillColorRGB(1, 0, 0, alpha=0.3)  # Color rojo, transparencia del 30%
                can.drawString(300, 400, "ANULADO")
                can.save()

                # Mover el puntero del buffer al inicio
                packet.seek(0)
                new_pdf = PdfReader(packet)
                page.merge_page(new_pdf.pages[0])
                pdf_writer.add_page(page)

            # Guardar el PDF final
            pdf_writer.write(final_buffer)

            # Mover el puntero del buffer final al inicio
            final_buffer.seek(0)
            # Copiar el contenido del buffer final al response
            response.write(final_buffer.read())
            return response
        else:
            # Si no está anulada, devolver el PDF generado por xhtml2pdf
            response.write(buffer.read())
            return response