from django.contrib import admin
from .models import Postagem, Categoria, Comentarios
# Register your models here.

class CategoriaAdm(admin.ModelAdmin):
    list_display = ['titulo', 'criada_em']

class PostagemAdm(admin.ModelAdmin):
    list_display = ['titulo', 'categoria',  'atualizada_em']
    list_filter = ['categoria']

class ComentarioAdm(admin.ModelAdmin):
    list_display = ['nome', 'comentario', 'criado_em']

admin.site.register(Categoria, CategoriaAdm)
admin.site.register(Postagem, PostagemAdm)
admin.site.register(Comentarios, ComentarioAdm)