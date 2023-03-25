from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from account.forms import UserRegisterForm

def editar_usuario(request):
    
    user = request.user   #capturo usuario
    
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
    return render(request, "account/form.html", context=context)

def register_account(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accountLogin")
        
    #form = UserCreationForm()
    form = UserRegisterForm()
    context = {
        "form" : form,
        "titulo": "Registra usuario",
        "enviar": "Registrar"
    }
    return render(request, "account/form.html", context=context)
            


def login_account(request):
    
    if request.method== "POST":
        form = AuthenticationForm(request, data=request.POST)   #cargo lo que me enviaron en el authentication form
        
        if form.is_valid():
            informacion = form.cleaned_data
            
            user = authenticate(username=informacion['username'], password=informacion['password'])
            if user is not None:
                login(request, user)
                
                
                return render(request, "account/form.html", context={"mensajes": ["Has iniciado sesion exitosamente"]})
            else:
                return render(request, "account/form.html", context={"mensajes": ["Intente nuevamente"]})
            

    form = AuthenticationForm()
    context={
        "form": form,
        "titulo": "Login",
        "enviar": "Iniciar"
    }
    return render(request, "account/form.html", context=context)