from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", tela_login),

    path("cadastro_usuario/", cadastro_usuario),

    path("home/", home),

    path("novo_chamado/", novo_chamado),
]