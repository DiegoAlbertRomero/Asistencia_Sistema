from django import forms
from .models import Periodo, Aula, Docente, Materia, Grupo, AsignacionAula

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['nombre', 'fecha_inicio', 'fecha_fin', 'es_periodo_actual']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'})
        }

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['nombre', 'capacidad']

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellidos', 'email']

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['codigo', 'nombre', 'descripcion']

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['codigo', 'materia', 'docente', 'periodo']

class AsignacionAulaForm(forms.ModelForm):
    class Meta:
        model = AsignacionAula
        fields = ['grupo', 'aula', 'dia', 'hora_inicio', 'hora_fin']
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'})
        }