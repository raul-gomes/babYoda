from django.shortcuts import render
from lista.util import getItem

# Create your views here.

def home(request):
    return render(request, "babYoda/home.html")

def lista(request):
    itens = getItem()
    return render(request, "babYoda/lista.html", {
        'itens': itens,
    })

def evento(request):
    return render(request, "babYoda/evento.html")

def album(request):
    return render(request, "babYoda/album.html")

def comentarios(request):
    return render(request, "babYoda/comentarios.html")
