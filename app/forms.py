from django import forms
from .models import orden_compra

class ordenForm(forms.ModelForm):
    class Meta:
        model = orden_compra
        fields = '__all__'