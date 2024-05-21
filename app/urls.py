
from django.urls import path
from .views import index,page_producto,crear_orden

urlpatterns = [
    path('', index,name='index'),
    path('page_producto',page_producto, name='page_producto'),
    path('crear_orden',crear_orden, name='crear_orden')
]
