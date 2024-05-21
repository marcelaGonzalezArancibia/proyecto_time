
from django.urls import path
from .views import index,page_producto

urlpatterns = [
    path('', index,name='index'),
    path('page_producto',page_producto, name='page_producto')
]
