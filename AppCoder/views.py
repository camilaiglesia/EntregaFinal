from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from AppCoder.models import  Bien, Comentario
from AppCoder.forms import BienForm, BusquedaBienForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Avatar

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
    return redirect("AppCoderBienes")

def detalle_bien(request,titulo):
    get_bien=Bien.objects.get(titulo=titulo)
    get_comentarios = Comentario.objects.filter(bien=get_bien)
           
    context = {
        "titulo": titulo,
        "bien": get_bien,
        "comentarios": get_comentarios
    }
    return render(request, "AppCoder/detalle_bien.html",context=context) 

@login_required
def comentar_bien(request,titulo):
    bien = Bien.objects.get(titulo=titulo)
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        comentario = Comentario(
            bien = bien,
            mensaje = mensaje,
            usuario = request.user
        )
        
        comentario.save()
        return redirect('AppCoderDetalleBien', titulo=titulo)

    return render(request, 'comentar_bien.html', {'bien': bien})
    


    
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


def panel_admin(request):
    return redirect('/admin/login/?next=/admin/')
    
def about(request):
    return render(request, 'about.html', {})

