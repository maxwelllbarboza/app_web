from django.urls import path, include
from galeria.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem/', imagem),
   
    
]