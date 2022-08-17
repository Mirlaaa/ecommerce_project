from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('produtos/',listar_produtos, name='produtos'),
    path('produtos/<int:pk>', produto_info, name='produto_info'),
    path('produtos_categoria/<str:categoria>',listar_categoria, name='produtos_categoria'),
    path('sobre/', sobre, name='sobre'),
]