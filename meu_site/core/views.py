from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produto, Contato

def home(request):
    produtos_destaque = Produto.objects.all()[:4]
    return render(request, 'core/home.html', {'produtos': produtos_destaque})

def sobre(request):
    return render(request, 'core/sobre.html')

def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'core/produtos.html', {'produtos': produtos})

def contato(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        mensagem = request.POST['mensagem']
        
        contato = Contato.objects.create(
            nome=nome, email=email, mensagem=mensagem
        )
        contato.save()
        messages.success(request, 'Mensagem enviada com sucesso!')
        return redirect('home')
    
    return render(request, 'core/contato.html')