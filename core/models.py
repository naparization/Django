from django.db import models

# Create your models here.

# Usar depois: models.ForeignKey(Artista, on_delete=models.CASCADE)

class Usuario(models.Model):
    Nome_Completo = models.TextField(max_length=100)
    Usuario = models.TextField(max_length=25)
    Senha = models.TextField(max_length=12)
    Eh_ADM = models.BooleanField(default=False)

class Categoria(models.Model):
    Nome = models.TextField(max_length=50)

class Chamado(models.Model):
    UsuarioId = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    CategoriaId = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Descricao = models.TextField()
    Prioridade = models.IntegerField(max_length=1)
    Esta_Aberto = models.BooleanField(default=False)

class Comentario(models.Model):
    Mensagem = models.TextField()
    ChamadoID = models.ForeignKey(Chamado, on_delete=models.CASCADE)



