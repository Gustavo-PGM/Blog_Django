from django.shortcuts import render, HttpResponseRedirect
from .models import Postagem, Categoria, Comentarios
from .forms import ComentarioForm
# Create your views here.


def postagem(request):
    ordenar = Postagem.objects.order_by('id')
    template_name = 'postagens.html'
    categorias = Categoria.objects.all()
    posts = Postagem.objects.all()
    contexto = {
        'posts':posts,
        'categorias':categorias
    }
    return render(request, template_name, contexto)

def detalhes(request, id):
    template_name = 'detalhes.html'
    post = Postagem.objects.get(id=id)
    comentarios =Comentarios.objects.filter(postagem_id=id)
    contexto = {
        'post':post,
        'comentarios':comentarios
    }
    return render(request, template_name, contexto)


def grupos(request, id):
    template_name = 'categorias.html'
    categorias = Categoria.objects.get(id=id)
    posta = Postagem.objects.get(id=id)
    contexto = {
        'categorias':categorias,
        'posta':posta
    }
    return render(request, template_name, contexto)


def adicionarcomentario(request, id):
    url = request.META.get('HTTP_REFERER') #Pega a url atual
    if request.method == 'POST': #Formulario é POST, pois tá enviando
        formulario = ComentarioForm(request.POST) #Peguei o corpo do forms
        if formulario.is_valid(): #Analisando se o forms é válido
            dados = Comentarios() #Peguei os dados
            dados.nome = formulario.cleaned_data['nome']
            dados.comentario = formulario.cleaned_data['comentario']
            dados.email = formulario.cleaned_data['email']
            dados.postagem_id = id
            dados.save()
            return HttpResponseRedirect(url)

        else:
            print(formulario.errors)
    return HttpResponseRedirect(url)