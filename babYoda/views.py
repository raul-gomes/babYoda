from django.shortcuts import render

# Create your views here.


app_name = 'babYoda'
nav = ['home', 'lista', 'evento', 'album', 'comentario']

def index(request):
    return render(request, "babYoda/home.html", {"itens": nav})
