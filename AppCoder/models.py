from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Mail: {self.mail}"
    
    
class Compra(models.Model):
    producto = models.CharField(max_length=50)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"Producto: {self.producto}, Precio: {self.precio}"
    
    
class Venta(models.Model):
    producto = models.CharField(max_length=50)
    precio= models.IntegerField()
    
    def __str__(self):
        return f"Producto: {self.producto}, Precio: {self.precio}"
    
class Bien(models.Model):
    nombre = models.CharField(max_length=50)
    caracteristica= models.CharField(max_length=50)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Caracteristica: {self.caracteristica}"
