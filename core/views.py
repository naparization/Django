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




    
