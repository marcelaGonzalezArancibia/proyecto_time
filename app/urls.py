
from django.urls import path
from .views import index,crearorden,listadoorden

urlpatterns = [
    path('', index,name='index'),
    path('crearorden',crearorden,name='crearorden'),
    path('listadoorden',listadoorden,name='listadoorden')
]
