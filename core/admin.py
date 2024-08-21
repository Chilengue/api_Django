from django.contrib import admin
from core.models import Avaliacao, Curso


@admin.register(Curso)
class CursoAdmin (admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'actualizacao', 'activo')

@admin.register(Avaliacao)
class AvalaicaoAdmin(admin.ModelAdmin):
    list_display=('curso', 'nome', 'email', 'avaliacao', 'criacao', 'actualizacao', 'activo')