from django.urls import path
from AppCoder.views import about, editar_bien, eliminar_bien, compras, ventas,bienes, crear_bien, crear_compra, crear_venta, busqueda_bien

urlpatterns = [
    path('about', about,name="AppCoderAbout"),
    path('compras', compras,name="AppCoderCompras"),
    path('ventas', ventas, name="AppCoderVentas"),
    path('bienes', bienes,name="AppCoderBienes"),
    path('bienes/eliminar/<nombre>', eliminar_bien ,name="AppCoderEliminarBien"),
    path('bienes/editar/<nombre>', editar_bien ,name="AppCoderEditarBien"),
    path('bienes/crear', crear_bien, name="AppCoderCrearBien"),
    path('bien/<nombre>/<caracteristica>', crear_bien, name="AppCoderBien"),
    path('compra/<producto>/<precio>', crear_compra, name="AppCoderCompra"),
    path('venta/<producto>/<precio>', crear_venta, name="AppCoderVenta"),
    path('busqueda_bien', busqueda_bien, name="AppCoderBuscarBien")
    ]