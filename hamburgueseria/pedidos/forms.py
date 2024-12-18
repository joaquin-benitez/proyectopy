from django import forms
from .models import Pedido
from menu_app.models import Hamburguesa


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['usuario','hamburguesa', 'cantidad']
    
    hamburguesa = forms.ModelChoiceField(queryset=Hamburguesa.objects.all(), label="Elige una Hamburguesa")
    cantidad = forms.IntegerField(min_value=1, label="Cantidad")