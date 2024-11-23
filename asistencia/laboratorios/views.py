from django.shortcuts import render
from django.http import JsonResponse
from .forms import RegistroLaboratorioForm
from .models import RegistroLaboratorio

# Create your views here.
def laboratorios(request):
    if request.method == 'POST':
        form = RegistroLaboratorioForm(request.POST)
        if form.is_valid():
            # Guardar el registro en la base de datos
            form.save()
            return JsonResponse({'success': True, 'mensaje': 'Registro guardado exitosamente'})
        else:
            return JsonResponse({'success': False, 'mensaje': 'Error al guardar el registro'})
    else:
        # Mostrar los registros y el formulario
        form = RegistroLaboratorioForm()
        registros = RegistroLaboratorio.objects.all()
        return render(request, 'laboratorios.html', {'form': form, 'registros': registros})
