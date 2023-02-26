from django.contrib import admin

from .models import Anunci
from .models import Usuari
from .models import Comentari

admin.site.register(Anunci)
admin.site.register(Usuari)
admin.site.register(Comentari)
