from django.contrib import admin

from pypro.turmas.models import Turma


class InscricaoInLine(admin.TabularInline):
    model = Turma.inscritos.through
    readonly_fields = ('data',)
    autocomplete_fields = ('usuario',)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    inlines = [InscricaoInLine]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
