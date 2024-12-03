from django import forms
from .models import Pedido
from menu_app.models import Hamburguesa

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_usuario', 'email', 'direccion', 'hamburguesa', 'cantidad']

    hamburguesa = forms.ModelChoiceField(queryset=Hamburguesa.objects.all(), empty_label="Selecciona una hamburguesa")