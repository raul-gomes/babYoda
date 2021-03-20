from django.urls import path
from . import views


app_name = "babYoda"
urlpatterns = [
    path('', views.home, name="home"),
    path('lista/', views.lista, name="lista"),
    path('evento/', views.evento, name="evento"),
    path('album/', views.album, name="album"),
    path('comentarios/', views.comentarios, name="comentarios")
]
