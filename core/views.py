import json

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def tela_login(request):

    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
            return redirect("/home/")

    return render(request, "core/login.html")

from core.models import Chamado, Identificador, Comentario

def cadastro_usuario(request):

    if request.method == "POST":
        nome = request.POST.get("nome")
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")

        novo_usuario = User.objects.create_user(
            username=usuario,
            first_name=nome,
            password=senha
        )

        Identificador.objects.create(
            Identificador_id=novo_usuario.id
        )

        

        return redirect("/")

    return render(request, "core/cadastro_usuario.html")

from django.shortcuts import redirect, render


# Create your views here.

@login_required
def home(request):
    is_staff = request.user.is_staff
    if (is_staff): 
        return render(request, 'core/home_usuario_adm.html')
    else:
        return render(request, 'core/home_usuario.html')

@login_required
def conclusao_chamado(request):
    return render(request, 'core/home_usuario_adm.html')

@login_required
def visualizar_conclusao_chamado(request):
    return render(request, 'core/home_usuario_adm.html')

@login_required
def adicionar_comentario(request):
    return render(request, 'core/home_usuario_adm.html')

@login_required
def comentarios(request, chamado_id):
    chamado = Chamado.objects.get(id=chamado_id)
    comentarios = Comentario.objects.filter(ChamadoID=chamado_id)
    return render(request, 'core/comentarios.html', {'chamado': chamado, 'comentarios': comentarios})

@login_required
def listar_chamados(request):
# (UsuarioId=request.user.id)
    is_staff = request.user.is_staff
    chamados = Chamado.objects.filter(UsuarioId=request.user.id)
    return render(request, 'core/lista_chamados.html', {'chamados': chamados, 'is_staff': is_staff})

@login_required
def listar_chamados_todos(request):
# (UsuarioId=request.user.id)
    is_staff = request.user.is_staff
    chamados = Chamado.objects.all()
    return render(request, 'core/lista_chamados.html', {'chamados': chamados, 'is_staff': is_staff})
    
@login_required
def novo_chamado(request):
    if request.method == "POST":
        descricao = request.POST.get('descricao')
        categoria_id = request.POST.get('categoria')
        Esta_Aberto = True
        prioridade = request.POST.get('prioridade')
        Chamado.objects.create(UsuarioId_id= request.user.id, CategoriaId_id = categoria_id, Descricao = descricao, Prioridade = prioridade, Esta_Aberto = Esta_Aberto)

        return redirect('home')
    return render(request, 'core/novo_chamado.html')

@login_required
def conclusao_chamado(request, chamado_id):
    if request.method == "POST":
        comentario = request.POST.get('comentario')
        Chamado.objects.filter(id=chamado_id).update(Esta_Aberto=False)
        return home(request)


    if (chamado_id < 1):
        return render(request, "core/login.html")

    chamado = Chamado.objects.get(id=chamado_id)

    return render(request, 'core/conclusao_chamado.html', {'chamado': chamado})




    
