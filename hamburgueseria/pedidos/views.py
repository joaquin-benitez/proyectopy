from django.shortcuts import render,get_object_or_404, redirect
from .forms import PedidoForm
from django.contrib.auth.decorators import login_required, user_passes_test
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
    query = request.GET.get('usuario', '')
    if query:
        pedidos = Pedido.objects.filter(usuario__username__icontains=query)
    else:
        pedidos = Pedido.objects.all()
    
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos, 'query': query})

# Verifica que el usuario sea admin
def is_admin(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_admin)
def admin_panel(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/admin_panel.html', {'pedidos': pedidos})

@user_passes_test(is_admin)
def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/editar_pedido.html', {'form': form})

@user_passes_test(is_admin)
def eliminar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return redirect('admin_panel')