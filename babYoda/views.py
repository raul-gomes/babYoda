from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "babYoda/home.html")

def lista(request):
    return render(request, "babYoda/lista.html")

def evento(request):
    return render(request, "babYoda/evento.html")

def album(request):
    return render(request, "babYoda/album.html")

def comentarios(request):
    return render(request, "babYoda/comentarios.html")
