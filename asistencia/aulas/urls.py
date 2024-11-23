from django.urls import path
from . import views

urlpatterns = [
    # Periodos
    path('periodos/', views.PeriodoListView.as_view(), name='lista_periodos'),
    path('periodos/nuevo/', views.PeriodoCreateView.as_view(), name='crear_periodo'),

    # Aulas
    path('aulas/', views.gestionar_aulas, name='gestionar_aulas'),
    path('aulas/asignacion/nueva/', views.crear_asignacion_aula, name='crear_asignacion'),
    path('aulas/asignacion/eliminar/<int:pk>/', views.eliminar_asignacion, name='eliminar_asignacion'),
]