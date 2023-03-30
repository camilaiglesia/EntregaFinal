from django.urls import path
from AppCoder.views import about, comentarios, detalle_bien, editar_bien, eliminar_bien,bienes, crear_bien, busqueda_bien
from account.views import profile

urlpatterns = [
    path('bienes/detalle/<titulo>', detalle_bien ,name="AppCoderDetalleBien"),
    path('about', about,name="AppCoderAbout"),
    path('comentario', comentarios,name="AppCoderComentarios"),
    path('bienes', bienes,name="AppCoderBienes"),
    path('bienes/eliminar/<titulo>', eliminar_bien ,name="AppCoderEliminarBien"),
    path('bienes/editar/<titulo>', editar_bien ,name="AppCoderEditarBien"),
    path('bienes/crear', crear_bien, name="AppCoderCrearBien"),
    path('bien/<titulo>/<subtitulo>', crear_bien, name="AppCoderBien"),
    path('busqueda_bien', busqueda_bien, name="AppCoderBuscarBien"),
    path('profile', profile, name="AppCoderProfile")
    ]