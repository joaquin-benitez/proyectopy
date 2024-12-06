from django.shortcuts import render, redirect
from .forms import PedidoForm
from django.contrib.auth.decorators import login_required
from .models import Pedido

@login_required
def realizar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user  
            pedido.save()
            return redirect('pedido_completado')  
    else:
        form = PedidoForm()
    
    return render(request, 'pedidos/realizar_pedido.html', {'form': form})

def pedido_completado(request):
    return render(request, 'pedidos/pedido_completado.html')

def lista_pedidos(request):
    pedidos = Pedido.objects.all()  
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})
