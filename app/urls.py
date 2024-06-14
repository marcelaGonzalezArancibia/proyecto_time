
from django.urls import path
from .views import index,crearorden,listadoorden,detalleorden,modificar,entrega

urlpatterns = [
    path('', index,name='index'),
    path('crearorden',crearorden,name='crearorden'),
    path('listadoorden',listadoorden,name='listadoorden'),
    path('detalleorden/<int:orden_id>/',detalleorden,name='detalleorden'),
    path('modificar/<int:orden_id>/',modificar,name='modificar'),
    path('entrega/<int:orden_id>/',entrega,name='entrega')
]
