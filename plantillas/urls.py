from django.urls import path
from . import views as plantillasViews

plantillas_patterns = ([
    path('tienda', plantillasViews.tienda, name='tienda'),
    path('administrador', plantillasViews.administrador, name='administrador'),
], "plantilla")