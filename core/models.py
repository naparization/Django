from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Usar depois: models.ForeignKey(Artista, on_delete=models.CASCADE)
class Usuario(models.Model):
    Nome_Completo = models.TextField(max_length=100, null=False)
    Usuario = models.TextField(max_length=25, null=False)
    Senha = models.TextField(max_length=12, null=False)
    Eh_ADM = models.BooleanField(default=False)
    CPF = models.TextField(max_length=11, null=True)

class Identificador(models.Model):
   Identificador = models.ForeignKey(User, on_delete=models.CASCADE, null=False) 
   
class Categoria(models.Model):
    Nome = models.TextField(max_length=50)

class Chamado(models.Model):
    UsuarioId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    CategoriaId = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    Descricao = models.TextField(default='Nada Informado.')
    Prioridade = models.IntegerField(max_length=1)
    Esta_Aberto = models.BooleanField(default=False)
    Comentario = models.TextField(default='Nada Informado.')

class Comentario(models.Model):
    Mensagem = models.TextField()
    UsuarioId = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ChamadoID = models.ForeignKey(Chamado, on_delete=models.CASCADE)



