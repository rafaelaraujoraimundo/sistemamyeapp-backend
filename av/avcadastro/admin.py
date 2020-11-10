from django.contrib import admin
from .models import PainelGeral, NotaFilial, DetalheIndicador, Nota, Indicador


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('nota', 'inicio', 'fim', 'ativo')


@admin.register(PainelGeral)
class PainelGeralAdmin(admin.ModelAdmin):
    list_display = ('idempresa', 'idfilial', 'periodo', 'idindicador', 'orcadometa',
                    'realizado', 'peso', 'pontuacao')


@admin.register(DetalheIndicador)
class DetalheIndicadorAdmin(admin.ModelAdmin):
    list_display = ('idempresa', 'idfilial', 'idindicador', 'descricao', 'meta', 'resultado')


@admin.register(Indicador)
class DetalheIndicadorAdmin(admin.ModelAdmin):
    list_display = ('idempresa', 'idfilial', 'codigo', 'descricao', 'peso')


@admin.register(NotaFilial)
class NotaFilialAdmin(admin.ModelAdmin):
    list_display = ('idempresa', 'idfilial', 'nota', 'periodo')




# Register your models here.
