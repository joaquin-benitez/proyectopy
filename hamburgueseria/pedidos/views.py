from django.shortcuts import render, redirect
from .forms import PedidoForm

def realizar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pedidos/confirmacion.html')  # Página de confirmación
    else:
        form = PedidoForm()
    return render(request, 'pedidos/pedido.html', {'form': form})
