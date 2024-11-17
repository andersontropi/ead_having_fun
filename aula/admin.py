from django.contrib import admin
from .models import Aula, Video, Usuario
from django.contrib.auth.admin import UserAdmin

# só existe porque a gente quer que no admin apareça o campo personalizado aulas_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('aulas_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Aula)
admin.site.register(Video)
admin.site.register(Usuario, UserAdmin)