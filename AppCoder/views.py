from django.http import HttpResponse
from django.shortcuts import redirect, render
from AppCoder.models import Compra, Venta, Bien
from AppCoder.forms import BienForm, CompraForm, VentaForm, BusquedaBienForm
from django.contrib.auth.decorators import login_required

def busqueda_bien(request):
    mi_formulario = BusquedaBienForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        bienes_filtrados = Bien.objects.filter(nombre__icontains=informacion["nombre"])
        context = {"bienes": bienes_filtrados
                   }
        return render(request, "AppCoder/busqueda_bien.html", context=context)



def crear_bien(request):
    if request.method == "POST":
        formBienes= BienForm(request.POST, request.FILES)
        
        if formBienes.is_valid():
            informacion = formBienes.cleaned_data
            bien_save = Bien(
                titulo=informacion["titulo"],
                subtitulo = informacion["subtitulo"],
                usuario = request.user,
                imagen=informacion["imagen"],
                descripcion=informacion["descripcion"]
            )
            bien_save.save()
            return redirect("AppCoderBienes")
            
    context = {
        "form" : BienForm()
    }
    return render(request, "AppCoder/crear_bien.html",context=context)    

def eliminar_bien(request,nombre):
    get_bien= Bien.objects.get(nombre=nombre)
    get_bien.delete()
    return redirect("AppCoderBienes")

def editar_bien(request,nombre):
    get_bien= Bien.objects.get(nombre=nombre) 
    
    if request.method == "POST":
        formBienes= BienForm(request.POST)
        
        if formBienes.is_valid():
            informacion = formBienes.cleaned_data
            
            get_bien.nombre=informacion["nombre"]
            get_bien.caracteristica = informacion["caracteristica"]
                                   
                            
            get_bien.save()
            return redirect("AppCoderBienes")
           
    context = {
        "nombre": nombre,
        "form" : BienForm(initial={
            "nombre":get_bien.nombre,
            "caracteristica":get_bien.caracteristica
        })
    }
    return render(request, "AppCoder/editar_bien.html",context=context) 

def bienes(request):
    all_bienes = Bien.objects.all()
    context = {"bienes" : all_bienes,
                "form_busqueda": BusquedaBienForm()
                } 
    return render(request, "AppCoder/bienes.html", context=context)


def crear_bien1(request, nombre, caracteristica):
    save_bien = Bien(nombre = nombre, caracteristica= caracteristica)
    save_bien.save()
    context = { "nombre": nombre}
    return render(request, "AppCoder/save_bien.html", context=context)

def compras(request):
    if request.method == "POST":
        formCompras= CompraForm(request.POST)
        
        if formCompras.is_valid():
            informacion = formCompras.cleaned_data
            compra_save = Compra(producto=informacion["producto"],
                                   precio = informacion["precio"]
                                   )
            compra_save.save()
    all_compras = Compra.objects.all()
    context = {"compras": all_compras,
               "form": CompraForm()}
    return render(request, "AppCoder/compras.html", context=context)

def crear_compra(request, producto, precio):
    save_compra = Compra(producto = producto, precio= int(precio))
    save_compra.save()
    context = { "producto": producto}
    return render(request, "AppCoder/save_compra.html", context=context)

def ventas(request):
    if request.method == "POST":
        formVentas= VentaForm(request.POST)
        
        if formVentas.is_valid():
            informacion = formVentas.cleaned_data
            venta_save = Venta(producto=informacion["producto"],
                                   precio = informacion["precio"]
                                   )
            venta_save.save()
    all_ventas = Venta.objects.all()
    context = {"ventas": all_ventas,
               "form": VentaForm()}
    return render(request, "AppCoder/ventas.html", context=context)

def crear_venta(request, producto, precio):
    save_venta = Venta(producto = producto, precio= int(precio))
    save_venta.save()
    context = { "producto": producto}
    return render(request, "AppCoder/save_venta.html", context=context)

def about(request):
    return render(request, 'about.html', {})
