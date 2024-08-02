from django.shortcuts import render
from .form import Newform
# Create your views here.
def acercadem(request):
    return render (request, 'acercademi.html')
def inicio(request):
    data={
        'forms': Newform()
    }
    return render(request,"index.html",data)

def galeria(request):
    return render(request,"galeria.html")

def contacto(request):
    return render(request, "contacto.html")

