from django.contrib import admin
from .models import Periodo, Aula, Docente, Materia, Grupo, AsignacionAula

admin.site.register(Periodo)
admin.site.register(Aula)
admin.site.register(Docente)
admin.site.register(Materia)
admin.site.register(Grupo)
admin.site.register(AsignacionAula)