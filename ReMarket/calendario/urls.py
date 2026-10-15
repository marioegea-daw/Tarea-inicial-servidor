from django.urls import path
from . import views

app_name = 'calendario'

urlpatterns = [
    path('', views.inicio, name='homepage'),
    path('fecha/<str:fecha>/', views.calendario, name='fecha'),
]