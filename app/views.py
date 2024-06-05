from django.shortcuts import render, redirect
from .models import orden


# Create your views here.
def index(request):
    return render(request,'index.html')

def orden(request):


    return render(request, 'orden.html')
 