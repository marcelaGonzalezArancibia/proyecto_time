
from django.urls import path
from .views import index,crearorden

urlpatterns = [
    path('', index,name='index'),
    path('crearorden',crearorden,name='crearorden'),
]
