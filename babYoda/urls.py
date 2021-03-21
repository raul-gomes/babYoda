from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "babYoda"

urlpatterns = [
    path('', views.home, name="home"),
    path('lista/', views.lista, name="lista"),
    path('evento/', views.evento, name="evento"),
    path('album/', views.album, name="album"),
    path('comentarios/', views.comentarios, name="comentarios")
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)