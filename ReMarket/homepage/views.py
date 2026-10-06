from django.shortcuts import render

# Vista principal de la aplicación Homepage
def homepage(request):
     # Carga la plantilla HTML de la aplicación
    return render(request, 'homepage/home.html')