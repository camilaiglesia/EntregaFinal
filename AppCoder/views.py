from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Usuario, Compra, Venta, Bien
from AppCoder.forms import UsuarioForm, BienForm, CompraForm, VentaForm, BusquedaBienForm

# Create your views here.

def busqueda_bien(request):
    mi_formulario = BusquedaBienForm(request.GET)
    if mi_formulario.is_valid():
        informacion = mi_formulario.cleaned_data
        bienes_filtrados = Bien.objects.filter(nombre__icontains=informacion["nombre"])
        context = {"bienes": bienes_filtrados
                   }
        return render(request, "AppCoder/busqueda_bien.html", context=context)




def usuarios(request):
    if request.method == "POST":
        mi_formulario= UsuarioForm(request.POST)
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario_save = Usuario(nombre=informacion["nombre"],
                                   apellido = informacion["apellido"],
                                   mail = informacion["mail"])
            usuario_save.save()
            
    all_usuarios = Usuario.objects.all()
    context = {"usuarios" : all_usuarios,
               "form": UsuarioForm()
               }
    
    return render(request, "AppCoder/usuarios.html", context=context)

def crear_usuario(request, nombre, apellido, mail):
    save_usuario = Usuario(nombre = nombre, apellido= apellido, mail = mail)
    save_usuario.save()
    context = { "nombre": nombre}
    return render(request, "AppCoder/save_usuario.html", context=context)
    

def bienes(request):
    if request.method == "POST":
        formBienes= BienForm(request.POST)
        
        if formBienes.is_valid():
            informacion = formBienes.cleaned_data
            bien_save = Bien(nombre=informacion["nombre"],
                            caracteristica = informacion["caracteristica"]
                                   )
            bien_save.save()
            
    all_bienes = Bien.objects.all()
    context = {"bienes" : all_bienes,
               "form": BienForm(),
                "form_busqueda": BusquedaBienForm()
                } 
    return render(request, "AppCoder/bienes.html", context=context)


def crear_bien(request, nombre, caracteristica):
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