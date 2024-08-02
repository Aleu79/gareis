from django.forms import ModelForm
from .models import datos

class Newform(ModelForm):
    class Meta:
        #traemos la tabla "datos"
        model = datos 
        fields = ['DNI', 'Nombre', 'Apellido'] # '__all__' esto es para llamar todos los campos
        
        