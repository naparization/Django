from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home_usuario.html')

def novo_chamado(request):
    return render(request, 'core/novo_chamado.html')
