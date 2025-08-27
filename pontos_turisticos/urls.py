from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pontos, name='listar_pontos'),
]
