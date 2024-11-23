from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Periodo, Aula, Docente, Materia, Grupo, AsignacionAula
from .forms import (
    PeriodoForm, AulaForm, DocenteForm, 
    MateriaForm, GrupoForm, AsignacionAulaForm
)

class PeriodoListView(ListView):
    model = Periodo
    template_name = 'aulas.html'
    context_object_name = 'periodos'

class PeriodoCreateView(CreateView):
    model = Periodo
    form_class = PeriodoForm
    template_name = 'periodo_form.html'
    success_url = reverse_lazy('lista_periodos')

def gestionar_aulas(request):
    periodo_actual = Periodo.objects.filter(es_periodo_actual=True).first()
    aulas = Aula.objects.all()
    asignaciones = AsignacionAula.objects.filter(grupo__periodo=periodo_actual)

    context = {
        'periodo_actual': periodo_actual,
        'aulas': aulas,
        'asignaciones': asignaciones
    }
    return render(request, 'aulas.html', context)

def crear_asignacion_aula(request):
    if request.method == 'POST':
        form = AsignacionAulaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_aulas')
    else:
        form = AsignacionAulaForm()
    return render(request, 'asignacion_form.html', {'form': form})

def eliminar_asignacion(request, pk):
    asignacion = get_object_or_404(AsignacionAula, pk=pk)
    asignacion.delete()
    return redirect('gestionar_aulas')