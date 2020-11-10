from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from core.models import Empresa, Filial, CustomUsuario, Modulos


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ('nomefilial', 'cnpj', 'criado', 'modificado', 'ativo')


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nomeempresa', 'criado', 'modificado', 'ativo')


@admin.register(Modulos)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('modulo', 'criado', 'modificado', 'ativo')
    

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone', 'idfilial', 'idempresa', 'perfil', 'idmodulos' )}),
        ('Permissões', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Data Importantes', {'fields': ('last_login', 'date_joined')}),
    )