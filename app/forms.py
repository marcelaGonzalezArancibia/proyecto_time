from django import forms
from .models import orden, ProductoOrden


class OrdenForm(forms.ModelForm):
    class Meta:
        model = orden
        fields = [
            'nombrevendedor', 'rutvendedor', 'nombreempresa', 'direccionv', 'telefonov',
            'correovendedor', 'nombrecliente', 'rutcliente', 'direccioncliente', 'correo',
            'telefonoc', 'valorNeto', 'iva', 'valorenvio', 'TotalAPagar'
        ]
        widgets = {
            'nombrevendedor': forms.TextInput(attrs={'class': 'form-control'}),
            'rutvendedor': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreempresa': forms.TextInput(attrs={'class': 'form-control'}),
            'direccionv': forms.TextInput(attrs={'class': 'form-control'}),
            'telefonov': forms.TextInput(attrs={'class': 'form-control'}),
            'correovendedor': forms.EmailInput(attrs={'class': 'form-control'}),
            'nombrecliente': forms.TextInput(attrs={'class': 'form-control'}),
            'rutcliente': forms.TextInput(attrs={'class': 'form-control'}),
            'direccioncliente': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefonoc': forms.TextInput(attrs={'class': 'form-control'}),
            'valorNeto': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control'}),
            'valorenvio': forms.NumberInput(attrs={'class': 'form-control'}),
            'TotalAPagar': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }

    # Agregamos este método para asegurarnos de que TotalAPagar sea incluido en el formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['TotalAPagar'].required = False
class ProductoOrdenForm(forms.ModelForm):
    class Meta:
        model = ProductoOrden
        fields = ['producto', 'descripcion', 'cantidad', 'preciounidad', 'totalproducto']
        widgets = {
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'preciounidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'totalproducto': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }