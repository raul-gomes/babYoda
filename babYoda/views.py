from django.shortcuts import render
from lista.util import getItem
from .forms import ListaForm
from lista.util import arrumalista, pega_lista


# Create your views here.

def home(request):
    return render(request, "babYoda/home.html")

def lista(request):

    itens = getItem()
    form = ListaForm()

    return render(request, "babYoda/lista.html", {
        'itens': itens,
        'form': form,
    })

def evento(request):
    return render(request, "babYoda/evento.html")

def album(request):
    return render(request, "babYoda/album.html")

def comentarios(request):
    return render(request, "babYoda/comentarios.html")

def carrinho(request):
    
    if request.method == 'POST':        
        form = ListaForm(request.POST)

        if form.is_valid():
            lista = form.cleaned_data
            arrumalista(lista['lista'])

    lista = pega_lista()
    
    return render(request, "babYoda/carrinho.html", {
        "lista": lista
    })
