
from django.urls import path
from .views import index,crearorden,listadoorden,detalleorden,entrega,DetalleOrdenPDF,rectificacion

urlpatterns = [
    path('', index,name='index'),
    path('crearorden',crearorden,name='crearorden'),
    path('listadoorden',listadoorden,name='listadoorden'),
    path('detalleorden/<int:orden_id>/',detalleorden,name='detalleorden'),
    path('entrega/<int:orden_id>/',entrega,name='entrega'),
    path('DetalleOrdenPDF/<int:orden_id>/',DetalleOrdenPDF.as_view(), name='DetalleOrdenPDF'),
    path('rectificacion/<int:orden_id>/',rectificacion,name='rectificacion')
]
