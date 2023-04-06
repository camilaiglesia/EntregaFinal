from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    
    class Meta:
        model = User
        fields = ("username", "email")
        
class UserEditForm(forms.ModelForm):
    imagen= forms.ImageField()
    class Meta:
        model = User
        fields = ['username', 'email','imagen']
       