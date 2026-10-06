from django.shortcuts import render

# Creamos una vista para la página de inicio
def homepage(request):
    return render(request, 'home.html')