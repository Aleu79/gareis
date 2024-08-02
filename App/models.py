from django.db import models
# Create your models here.

class datos(models.Model):
    DNI=models.IntegerField(primary_key=True)
    Nombre=models.TextField(max_length=35)
    Apellido=models.TextField(max_length=35)
    Edad=models.IntegerField()
    Fecha_Nacimiento=models.DateField()
    
    def __int__(self):
        self.DNI +' y ' + self.Nombre
    
    