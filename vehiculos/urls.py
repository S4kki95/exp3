from django.urls import path
from .views import index,otra,crear,eliminar,modificar, registrar, mostrar

urlpatterns=[
    path('', index, name="index"), 
    path('otra/', otra, name="otra"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/',mostrar, name="mostrar")
    
]