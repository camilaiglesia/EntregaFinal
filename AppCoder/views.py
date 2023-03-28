from django.http import HttpResponse
from django.shortcuts import redirect, render
from AppCoder.models import Compra, Venta, Bien
from AppCoder.forms import BienForm, Comentario, CompraForm, VentaForm, BusquedaBienForm
from django.contrib.auth.decorators import login_required

def busqueda_bien(request):
    mi_formulario = BusquedaBienForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        bienes_filtrados = Bien.objects.filter(titulo__icontains=informacion["titulo"])
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

def eliminar_bien(request,titulo):
    bien = Bien.objects.get(titulo = titulo)
    bien.delete()
    bien = Bien.objects.all()
    context = {
        "bienes": bienes
    }
    return render(request,"AppCoder/bienes.html", context=context)

def detalle_bien(request,titulo):
    get_bien=Bien.objects.get(titulo=titulo)
    if request.method == "POST":
            pass
           
    context = {
        "titulo": titulo,
        "bien": get_bien,
    }
    return render(request, "AppCoder/detalle_bien.html",context=context)     


def editar_bien(request,titulo):
    get_bien= Bien.objects.get(titulo=titulo) 
    
    if request.method == "POST":
        formBienes= BienForm(request.POST,request.FILES)
       
        if formBienes.is_valid():
            informacion = formBienes.cleaned_data
            
            get_bien.titulo=informacion["titulo"]
            get_bien.subtitulo = informacion["subtitulo"]
            get_bien.descripcion = informacion["descripcion"]                       
            get_bien.imagen = informacion["imagen"]       
                     
            get_bien.save()
            return redirect("AppCoderBienes")
           
    context = {
        "titulo": titulo,
        "form" : BienForm(initial={
            "titulo":get_bien.titulo,
            "subtitulo":get_bien.subtitulo,
            "imagen.url": get_bien.imagen.url if get_bien.imagen else None
            
        })
    }
    
    return render(request, "AppCoder/editar_bien.html",context=context) 

def bienes(request):
    all_bienes = Bien.objects.all()
    context = {"bienes" : all_bienes,
                "form_busqueda": BusquedaBienForm()
                } 
    return render(request, "AppCoder/bienes.html", context=context)


def crear_bien1(request, titulo, subtitulo):
    save_bien = Bien(titulo = titulo, subtitulo= subtitulo)
    save_bien.save()
    context = { "titulo": titulo}
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
