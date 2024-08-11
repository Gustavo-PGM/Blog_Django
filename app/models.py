from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Postagem(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=False)
    texto = RichTextUploadingField()
    imagens = models.ImageField(upload_to = 'imagens/' ,blank=True)
    criada_em =models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['id']

class Comentarios(models.Model):
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=80, blank=False)
    email = models.EmailField(blank=False)
    comentario = models.TextField(blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['id']

    def __str__(self):
        return self.comentario