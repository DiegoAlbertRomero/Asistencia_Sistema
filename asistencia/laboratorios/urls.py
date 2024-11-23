from django.urls import path
from laboratorios.views import laboratorios

urlpatterns = [
    path('', laboratorios, name = 'laboratorios'),
]
