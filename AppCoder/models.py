
from django.db import models
from django.contrib.auth.models import User



# Create your models here.  
    

class Bien(models.Model):
    usuario = models.ForeignKey(to=User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="bienes/", null=True, blank=True)
    
    def __str__(self):
        return f"Titulo: {self.titulo}, Subtitulo: {self.subtitulo}"

class Comentario(models.Model):
    usuario = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    bien = models.ForeignKey(Bien, related_name='bien_recibido', on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
    


class Profile(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.EmailField()
    imagen = models.ImageField(upload_to="avatares/", null=True, blank=True)
        
    
    def __str__(self):
        return f"usuario: {self.usuario}, email: {self.email}, imagen: {self.imagen}"
    
