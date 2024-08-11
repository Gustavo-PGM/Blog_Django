from django.urls import path
from . import views

urlpatterns = [
    path('', views.postagem, name='postagens'),
    path('detalhes/<int:id>/', views.detalhes, name='detalhes'),
    path('categorias/<int:id>/', views.grupos, name='grupos'),
    path('adicionarcomentario/<int:id>/', views.adicionarcomentario, name='comentarios'),

]