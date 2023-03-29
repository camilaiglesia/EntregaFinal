from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    imagen= forms.ImageField()
    
    class Meta:
        model = User
        fields = ("username", "email", "imagen")
        
class UserEditForm(forms.ModelForm):
  
    class Meta:
        model = User
        fields = ['username', 'email']
       