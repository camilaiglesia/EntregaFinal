from enum import unique
from django import forms
from django.contrib.auth.models import User

from AppCoder.models import Bien

 
 
class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = ("titulo","subtitulo","descripcion","imagen")
    
class BusquedaBienForm(forms.Form):
    titulo = forms.CharField(min_length=2, max_length=50)
    
  
    
class ComentForm(forms.Form):
    comentario = forms.CharField(max_length=200)
    
   