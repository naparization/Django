from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def tela_login(request):

    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
            return redirect("/home/")

    return render(request, "core/login.html")


def cadastro_usuario(request):

    if request.method == "POST":
        nome = request.POST.get("nome")
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        User.objects.create_user(
            username=usuario,
            first_name=nome,
            password=senha
        )

        return redirect("/")

    return render(request, "core/cadastro_usuario.html")

from django.shortcuts import redirect, render

from core.models import Chamado

# Create your views here.

def home(request):
    return render(request, 'core/home_usuario.html')


def novo_chamado(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')
        prioridade = request.POST.get('prioridade')
        Chamado.objects.create(UsuarioId_id= 1, CategoriaId_id = categoria_id, Descricao = descricao, Prioridade = prioridade)

        return redirect('home')
    return render(request, 'core/novo_chamado.html')




    
