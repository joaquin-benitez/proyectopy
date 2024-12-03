from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_usuario', 'email', 'direccion', 'hamburguesa', 'cantidad']

