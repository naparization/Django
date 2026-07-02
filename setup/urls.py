from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tela_login),
    path("cadastro_usuario/", cadastro_usuario),
    path("home/", home, name='home'),
    path("novo_chamado/", novo_chamado, name='novo_chamado'),
    path("lista_chamados/", listar_chamados, name='listar_chamados'),
    path("funcionario/lista_chamados/", listar_chamados_todos, name='listar_chamados_todos'),
    path("<int:chamado_id>/conclusao_chamado/", conclusao_chamado, name='conclusao_chamado' ),
    path("<int:chamado_id>/visualizar_conclusao_chamado/", visualizar_conclusao_chamado, name='visualizar_conclusao_chamado'),
    path("<int:chamado_id>/comentarios/", comentarios, name='comentarios'),
    path("<int:chamado_id>/adicionar_comentario/", adicionar_comentario, name='adicionar_comentario'),
    path("<int:chamado_id>/deletar_chamado/", deletar_chamado, name='deletar_chamado'),
    path("logout/", fazer_logout, name='fazer_logout'),
]