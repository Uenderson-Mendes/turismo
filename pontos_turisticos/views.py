from django.shortcuts import render
from .models import PontoTuristico

def listar_pontos(request):
    pontos = PontoTuristico.objects.all()
    return render(request, 'pontos_turisticos/listar.html', {'pontos': pontos})
