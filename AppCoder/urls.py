from django.urls import path
from AppCoder.views import usuarios, compras, ventas, crear_usuario, bienes, crear_bien

urlpatterns = [
    path('usuarios', usuarios, name="AppCoderUsuarios" ),
    path('compras', compras,name="AppCoderCompras"),
    path('ventas', ventas, name="AppCoderVentas"),
    path('bienes', bienes,name="AppCoderBienes"),
    path('usuario/<nombre>/<apellido>/<mail>', crear_usuario, name="AppCoderUsuario"),
    path('bien/<nombre>/<caracteristica>', crear_bien, name="AppCoderBien")
    ]