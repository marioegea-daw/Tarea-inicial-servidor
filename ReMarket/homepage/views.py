from django.shortcuts import render
from ReMarket.session_utils import contar_visita


def homepage(request):
    visitas = contar_visita(request)
    contexto = {
        'visitas': visitas,
    }
    return render(request, 'homepage/home.html', contexto)