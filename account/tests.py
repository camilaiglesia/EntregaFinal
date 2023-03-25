from django.test import TestCase
from django.urls import reverse
from AppCoder.models import Bien

class BienTestCase(TestCase):       #base iniciar de las pruebas
    
    def setUp(self):            #creando pruebas
        Bien.objects.create(nombre="Computadora", caracteristica="Dell")
        Bien.objects.create(nombre="Smartphone", caracteristica="Samsung")
        
        
        
    def test_creando_bienes(self):
        comp= Bien.objects.get(caracteristica="Dell")
        smart= Bien.objects.get(caracteristica="Samsung")
        self.assertEqual(comp.nombre,'Computadora')       #si lo que traje de la bd es lo mismo que habia enviado
        self.assertEqual(smart.nombre,'Smartphone')
        
        
class ViewTests(TestCase):
    
    def test_no_questions(self):
        response= self.client.get(reverse('AppCoderBienes'))    #creando una interfaz web
        self.assertEqual(response.status_code, 200)         
        self.assertContains(response, "Creacion del producto")
        
    def test_past_question(self):
        bien = Bien.objects.create(nombre="Computadora", caracteristica="Dell")
        response= self.client.get(reverse('AppCoderBienes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nombre: Computadora, Caracteristica: Dell")