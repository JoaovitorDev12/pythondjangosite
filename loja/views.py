from django.shortcuts import render
from .models import Produto
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def catalogo(request):
    produtos = Produto.objects.all()
    return render(request, 'loja/catalogo.html', {'produtos': produtos})
def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'cadastro.html', {'form': form})