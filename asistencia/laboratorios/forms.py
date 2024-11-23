from django import forms
from .models import RegistroLaboratorio

class RegistroLaboratorioForm(forms.ModelForm):
    class Meta:
        model = RegistroLaboratorio
        fields = ['aula', 'fecha', 'hora', 'nombre_docente', 'materia', 'nombre_practica', 'carrera', 'estudiantes_hombres', 'estudiantes_mujeres']

    fecha = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    hora = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time'}))