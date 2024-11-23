from django.db import models

class RegistroLaboratorio(models.Model):
    aula = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    nombre_docente = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    nombre_practica = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    estudiantes_hombres = models.IntegerField()
    estudiantes_mujeres = models.IntegerField()

    def _str_(self):
        return f'{self.nombre_practica} en {self.aula} el {self.fecha}'