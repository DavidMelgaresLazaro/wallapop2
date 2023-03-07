from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User




from .models import Anunci
from .models import Usuari
from .models import Comentari





class UsuariInline(admin.StackedInline):
    model = Usuari
    can_delete = False
    verbose_name_plural = 'Usuaris'


class UserAdmin(BaseUserAdmin):
    inlines = (UsuariInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Anunci)
admin.site.register(Comentari)



