from enum import unique
from django import forms


    
 
class BienForm(forms.Form):
    nombre = forms.CharField(min_length=2, max_length=50)
    caracteristica = forms.CharField(min_length=2, max_length=50)
    
class BusquedaBienForm(forms.Form):
    nombre = forms.CharField(min_length=2, max_length=50)
    
  
    
class CompraForm(forms.Form):
    producto = forms.CharField(min_length=2, max_length=50)
    precio = forms.IntegerField()
   
   
    
class VentaForm(forms.Form):
    producto = forms.CharField(min_length=2, max_length=50)
    precio = forms.IntegerField()
    