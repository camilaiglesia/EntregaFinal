
from django.db import models
from django.contrib.auth.models import User


# Create your models here.  
    
class Compra(models.Model):
    producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"Producto: {self.producto}, Precio: {self.precio}"
    
    

class Bien(models.Model):
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="bienes/", null=True, blank=True)
    def __str__(self):
        return f"Titulo: {self.titulo}, Subtitulo: {self.subtitulo}"

class Comentar(models.Model):
    comentario: models.CharField(max_length=200)
    
class Profile(models.Model):
    username = models.CharField(max_length=50)
    email= models.EmailField()
    
    