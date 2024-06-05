
from django.urls import path
from .views import index,orden

urlpatterns = [
    path('', index,name='index'),
    path('orden',orden,name='orden'),
]
