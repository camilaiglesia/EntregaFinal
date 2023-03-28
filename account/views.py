import logging
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from account.forms import UserRegisterForm
from account.models import Avatar

def editar_usuario(request):
    user = request.user   #capturo usuario
  
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST, request.FILES)
        
        if form.is_valid():
            informacion = form.cleaned_data
            user.username = informacion["username"]
            user.email= informacion["email"]
            user.is_staff= informacion["is_staff"]
            
            try:           #edicion
                user.avatar.imagen= informacion["imagen"]
            except:                   #creacion
                avatar = Avatar(user=user, imagen=informacion["imagen"])
                avatar.save()
            
            user.save()
            return redirect("accountLogin")

    form = UserRegisterForm(initial={
        "username":user.username, 
        "email":user.email,     #tengo que estar loggeada
        "is_staff":user.is_staff
        })
    context= {
        "form": form,
        "titulo": "Editar usuario",
        "enviar": "Editar"
    }
    return render(request, "form.html", context=context)

def register_account(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST, request.FILES)
        logging.error(form.errors)
        if form.is_valid():
            logging.error("Estamos guardando")
            form.save()
            return redirect("accountLogin")
        
    #form = UserCreationForm()
    form = UserRegisterForm()
    context = {
        "form" : form,
        "titulo": "Registrar usuario",
        "enviar": "Registrar"
    }
    return render(request, "form.html", context=context)
            


def login_account(request):
    
    if request.method== "POST":
        form = AuthenticationForm(request, data=request.POST)   #cargo lo que me enviaron en el authentication form
        
        if form.is_valid():
            informacion = form.cleaned_data
            
            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user is not None:
                login(request, user)
                
                
                return render(request, "form.html", context={"mensajes": ["Has iniciado sesion exitosamente"]})
            else:
                return render(request, "form.html", context={"mensajes": ["Intente nuevamente"]})
            

    form = AuthenticationForm()
    context={
        "form": form,
        "titulo": "Login",
        "enviar": "Iniciar"
    }
    return render(request, "form.html", context=context)


def inicio(request):
    return redirect("accountLogin")