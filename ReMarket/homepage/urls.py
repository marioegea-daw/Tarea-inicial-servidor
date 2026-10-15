from django.urls import path
from . import views

app_name = 'homepage'

 # Conecta la URL de la aplicación con la vista homepage
urlpatterns = [
    path('', views.homepage, name='homepage'),
]