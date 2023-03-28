from django.urls import path
from AppCoder.views import about, detalle_bien, editar_bien, eliminar_bien, compras, ventas,bienes, crear_bien, crear_compra, crear_venta, busqueda_bien

urlpatterns = [
    path('bienes/detalle/<titulo>', detalle_bien ,name="AppCoderDetalleBien"),
    path('about', about,name="AppCoderAbout"),
    path('compras', compras,name="AppCoderCompras"),
    path('ventas', ventas, name="AppCoderVentas"),
    path('bienes', bienes,name="AppCoderBienes"),
    path('bienes/eliminar/<titulo>', eliminar_bien ,name="AppCoderEliminarBien"),
    path('bienes/editar/<titulo>', editar_bien ,name="AppCoderEditarBien"),
    path('bienes/crear', crear_bien, name="AppCoderCrearBien"),
    path('bien/<titulo>/<subtitulo>', crear_bien, name="AppCoderBien"),
    path('compra/<producto>/<precio>', crear_compra, name="AppCoderCompra"),
    path('venta/<producto>/<precio>', crear_venta, name="AppCoderVenta"),
    path('busqueda_bien', busqueda_bien, name="AppCoderBuscarBien")
    ]