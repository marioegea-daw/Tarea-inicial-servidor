from django.shortcuts import render
from ReMarket.session_utils import contar_visita

# Vista principal de la aplicación Homepage
def homepage(request):
     # Carga la plantilla HTML de la aplicación
    return render(request, 'homepage/home.html')
    visitas = contar_visita(request)
    contexto = {
        'visitas': visitas,
    }
    return render(request, 'homepage/home.html', contexto)
