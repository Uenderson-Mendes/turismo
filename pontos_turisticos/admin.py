from django.contrib import admin
from .models import PontoTuristico

# Registrar o modelo no admin
@admin.register(PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'endereco', 'latitude', 'longitude')
    search_fields = ('nome', 'categoria', 'endereco')
    list_filter = ('categoria',)                  # filtro lateral

