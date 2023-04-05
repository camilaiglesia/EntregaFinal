from django.urls import path
from AppCoder.views import about, comentar_bien, detalle_bien, editar_bien, eliminar_bien,bienes, crear_bien, busqueda_bien, mensajes
from account.views import profile

urlpatterns = [
    path('bienes/detalle/<titulo>', detalle_bien ,name="AppCoderDetalleBien"),
    path('about', about,name="AppCoderAbout"),
    path('mensajes', mensajes,name="AppCoderMensajes"),
    path('bienes', bienes,name="AppCoderBienes"),
    path('bienes/eliminar/<titulo>', eliminar_bien ,name="AppCoderEliminarBien"),
    path('bienes/editar/<titulo>', editar_bien ,name="AppCoderEditarBien"),
    path('bienes/crear', crear_bien, name="AppCoderCrearBien"),
    path('bien/<titulo>/<subtitulo>', crear_bien, name="AppCoderBien"),
    path('busqueda_bien', busqueda_bien, name="AppCoderBuscarBien"),
    path('profile', profile, name="AppCoderProfile"),
    path('comentar/<titulo>', comentar_bien, name="AppCoderComentarBien")
    ]