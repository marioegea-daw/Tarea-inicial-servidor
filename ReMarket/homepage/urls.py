from django.urls import path
from . import views

 # Conecta la URL de la aplicación con la vista homepage
urlpatterns = [
    path('', views.homepage),
]