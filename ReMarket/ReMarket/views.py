
from django.shortcuts import render


# Muestra la página principal de acogida
def index(request):
    return render(request, 'homepage/index.html')


# Muestra la página de contacto
def contact(request):
    return render(request, 'homepage/contact.html')
