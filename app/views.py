from django.shortcuts import render
from .forms import ordenForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def page_producto(request):
    return render(request,'producto.html')


def crear_orden(request):
    data = {
        'form': ordenForm()
    }

    if request.method == 'POST':
        formulario = ordenForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "orden agregada correctamente"
        else:
            data['form'] = formulario
    return render(request,'crear_orden.html',data)