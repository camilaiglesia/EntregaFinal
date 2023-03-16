from django.contrib import admin

from AppCoder.models import Usuario, Bien, Compra, Venta

# Register your models here.

admin.site.register(Usuario)

admin.site.register(Bien)

admin.site.register(Compra)

admin.site.register(Venta)