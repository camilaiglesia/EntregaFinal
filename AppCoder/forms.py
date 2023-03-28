from enum import unique
from django import forms

from AppCoder.models import Bien

 
class Comentario(forms.ModelForm):
    class Meta:
        model = Bien
        fields = ("titulo","subtitulo","descripcion","imagen")
    
 
class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
        fields = ("titulo","subtitulo","descripcion","imagen")
    
class BusquedaBienForm(forms.Form):
    titulo = forms.CharField(min_length=2, max_length=50)
    
  
    
class CompraForm(forms.Form):
    producto = forms.CharField(min_length=2, max_length=50)
    precio = forms.IntegerField()
   
   
    
class VentaForm(forms.Form):
    producto = forms.CharField(min_length=2, max_length=50)
    precio = forms.IntegerField()
    