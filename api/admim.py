from django.contrib import admin
from .models import curso, Avaliacao

@admin.register(curso)
class CursoAdmin (admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')

@admin.register(Avaliacao):
class AvalaicaoAdmin(admin.modelAdmin)