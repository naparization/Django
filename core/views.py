import json

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def tela_login(request):

    if request.method == "POST":
        usuario = request.POST.get("usuario")
        senha = request.POST.get("senha")
        
        user = authenticate(username=usuario, password=senha)

        if user:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso.')
            return redirect("/home/")
        else:
            messages.error(request, 'Não foi possível realizar login, por favor tente novamente.')

    return render(request, "core/login.html")

from core.models import Categoria, Chamado, Identificador, Comentario

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
    user = request.user.id
    Usuario = User.objects.get(id = user)
    if (is_staff): 
        return render(request, 'core/home_usuario_adm.html', {'Usuario': Usuario})
    else:
        return render(request, 'core/home_usuario.html')
    
@login_required
def fazer_logout(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso, até a próxima.')
    return redirect("/")

@login_required
def conclusao_chamado(request):
    return render(request, 'core/home_usuario_adm.html')

@login_required
def visualizar_conclusao_chamado(request):
    return render(request, 'core/home_usuario_adm.html')

@login_required
def adicionar_comentario(request, chamado_id):

    chamado = Chamado.objects.get(id=chamado_id)

    if request.method == "POST":
        comentario = request.POST.get("comentario")
        user_id = request.user

        try:
            Comentario.objects.create(
                Mensagem=comentario,
                UsuarioId=user_id,
                ChamadoID=chamado
                )
            messages.success(request, 'Comentário adicionado.')
        except: 
            messages.error(request, 'Não foi possível adicionar comentários.')


        return comentarios(request, chamado_id)

    return render(
        request,
        "core/adicionar_comentario.html",
        {
            "chamado": chamado
        }
    )
    

@login_required
def comentarios(request, chamado_id):
    id_usuario = request.user.id
    is_staff = request.user.is_staff
    chamado = Chamado.objects.get(id=chamado_id)
    comentarios = Comentario.objects.filter(ChamadoID=chamado_id)
    return render(request, 'core/comentarios.html', {'chamado': chamado, 'comentarios': comentarios, 'is_staff': is_staff, 'id_usuario': id_usuario})

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
        try:
            Chamado.objects.create(UsuarioId_id= request.user.id, CategoriaId_id = categoria_id, Descricao = descricao, Prioridade = prioridade, Esta_Aberto = Esta_Aberto)
            messages.success(request, 'Chamado criado.')
        except:
            messages.error(request, 'Ocorreu um erro ao gerar este chamado. Tente novamente.')

        return redirect('home')
    categorias = Categoria.objects.all() 
    return render(request, 'core/novo_chamado.html', {'categorias': categorias})

@login_required
def conclusao_chamado(request, chamado_id):
    if request.method == "POST":
        comentario = request.POST.get('comentario')
        Chamado.objects.filter(id=chamado_id).update(Esta_Aberto=False, Comentario=comentario)
        messages.success(request, 'Chamado concluído.')
        return home(request)


    if (chamado_id < 1):
        messages.error(request, 'Ocorreu um erro.')
        return render(request, "core/login.html")

    chamado = Chamado.objects.get(id=chamado_id)

    return render(request, 'core/conclusao_chamado.html', {'chamado': chamado})

@login_required
def deletar_chamado(request, chamado_id):
    is_staff = request.user.is_staff
    user_id = request.user.id
    chamado = Chamado.objects.get(id = chamado_id)
    print(chamado.UsuarioId_id)


    if (chamado.UsuarioId_id == user_id or is_staff):
        chamado.delete()
        messages.success(request, 'Chamado cancelado.')
        return home(request)
        
    else:
        return home(request)

@login_required
def deletar_comentario(request, comentario_id):
    is_staff = request.user.is_staff
    user_id = request.user.id
    comentario = Comentario.objects.get(id = comentario_id)
    print(comentario.UsuarioId_id)


    if (comentario.UsuarioId_id == user_id or is_staff):
        comentario.delete()
        messages.success(request, 'Comentário removido.')
        return home(request)
        
    else:
        messages.error(request, 'Ação não permitida.')
        return home(request)


    
