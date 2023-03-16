from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Usuario, Compra,Venta, Bien

# Create your views here.

def usuarios(request):
    all_usuarios = Usuario.objects.all()
    context = {"usuarios" : all_usuarios }
    
    return render(request, "AppCoder/usuarios.html", context=context)

def crear_usuario(request, nombre, apellido, mail):
    save_usuario = Usuario(nombre = nombre, apellido= apellido, mail = mail)
    save_usuario.save()
    context = { "nombre": nombre}
    return render(request, "AppCoder/save_usuarios.html", context=context)
    

def bienes(request):
    all_bienes = Bien.objects.all()
    context = {"bienes" : all_bienes }
    return render(request, "AppCoder/bienes.html", context=context)


def crear_bien(request, nombre, caracteristica):
    save_bien = Bien(nombre = nombre, caracteristica= caracteristica)
    save_bien.save()
    context = { "nombre": nombre}
    return render(request, "AppCoder/save_bien.html", context=context)

def compras(request):
    all_compras = Compra.objects.all()
    context = {"compras": all_compras}
    return render(request, "AppCoder/compras.html", context=context)

def crear_compra(request, producto, precio):
    save_compra = Compra(producto = producto, precio= int(precio))
    save_compra.save()
    context = { "producto": producto}
    return render(request, "AppCoder/save_compra.html", context=context)

def ventas(request):
    all_ventas = Venta.objects.all()
    context = {"ventas": all_ventas}
    return render(request, "AppCoder/ventas.html", context=context)

def crear_venta(request, producto, precio):
    save_venta = Venta(producto = producto, precio= int(precio))
    save_venta.save()
    context = { "producto": producto}
    return render(request, "AppCoder/save_venta.html", context=context)