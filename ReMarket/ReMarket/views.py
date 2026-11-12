
from django.shortcuts import render

# Importamos la función que cuenta las visitas de cada sesión.
from ReMarket.session_utils import contar_visita


# Muestra la página principal de acogida.
def index(request):

    # Recuperamos e incrementamos el contador de visitas.
    visitas = contar_visita(request)

    # Preparamos los datos que enviaremos al HTML.
    contexto = {
        'visitas': visitas,
    }

    # Mostramos la página principal enviándole el contador.
    return render(request, 'homepage/index.html', contexto)


# Muestra la página de contacto.
def contact(request):

    # Recuperamos e incrementamos el contador de visitas.
    visitas = contar_visita(request)

    # Preparamos los datos que enviaremos al HTML.
    contexto = {
        'visitas': visitas,
    }

    # Mostramos la página de contacto enviándole el contador.
    return render(request, 'homepage/contact.html', contexto)
