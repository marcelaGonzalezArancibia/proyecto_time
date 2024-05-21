from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def page_producto(request):
    return render(request,'producto.html')


def crear_orden(request):
    return render(request,'crear_orden.html')